#!/usr/bin/env python3
"""Fix 5 issues: cat shape, TV position, room barriers, door interaction, quest guidance."""
PATH = "/home/kiki/Documents/gameBuild/desktopNavigator/desktopNavigator.html"
BAK = PATH + ".bak_fixes"

import shutil, re
with open(PATH) as f:
    c = f.read()
shutil.copy2(PATH, BAK)

orig = c

# ===== 1. FIX TV POSITION — Move in front of couch with 1m gap =====
# Couch center: (-12, .75, 6), depth 3.5 → front edge at z=7.75
# TV should be at z=7.75+0.5+1.0 = ~9.25 with 1m gap
# TV stand at floor level, screen facing couch

# Current TV: tvS at (-14, .1, 6), tvB at (-14, 1.5, 5.4), screen at (-14, 1.5, 5.47)
# New position: directly in front of couch center (-12, ...) not at -14

# Replace tvS (TV stand/surface)
old = "const tvS=new THREE.Mesh(new THREE.BoxGeometry(3,.2,1.5),warmMat(0x1a1a1a,.4,.5));tvS.position.set(-14,.1,6);tvS.receiveShadow=true;scene.add(tvS);allBuildingMeshes.push(tvS);addSB(1.5,.1,.75,-14,.1,6);"
new = "const tvS=new THREE.Mesh(new THREE.BoxGeometry(2.2,.2,1.2),warmMat(0x1a1a1a,.4,.5));tvS.position.set(-12,.1,9);tvS.receiveShadow=true;scene.add(tvS);allBuildingMeshes.push(tvS);addSB(1.1,.1,.6,-12,.1,9);"
c = c.replace(old, new)

# Replace tvB (TV body/back)
old = "const tvB=new THREE.Mesh(new THREE.BoxGeometry(2.4,1.8,.12),warmMat(0x1a1a1a,.3,.6));tvB.position.set(-14,1.5,5.4);tvB.castShadow=true;scene.add(tvB);allBuildingMeshes.push(tvB);"
new = "const tvB=new THREE.Mesh(new THREE.BoxGeometry(2,1.6,.1),warmMat(0x1a1a1a,.3,.6));tvB.position.set(-12,1.5,8.94);tvB.castShadow=true;scene.add(tvB);allBuildingMeshes.push(tvB);"
c = c.replace(old, new)

# Replace screen (sc) position
old = "const sc=new THREE.Mesh(new THREE.PlaneGeometry(2.1,1.5),scMat);sc.position.set(-14,1.5,5.47);"
new = "const sc=new THREE.Mesh(new THREE.PlaneGeometry(1.8,1.4),scMat);sc.position.set(-12,1.5,9.01);"
c = c.replace(old, new)

# Replace tvI (interactable) position
old = "tvI=new Body({pos:new THREE.Vector3(-14,1.5,5.4),hs:new THREE.Vector3(1.2,.9,.1),static:true,tag:'tv',isInteractable:true,interactType:'activate',interactPrompt:'Turn on TV',data:{points:5}});"
new = "tvI=new Body({pos:new THREE.Vector3(-12,1.5,9),hs:new THREE.Vector3(1,.8,.1),static:true,tag:'tv',isInteractable:true,interactType:'activate',interactPrompt:'Turn on TV',data:{points:5}});"
c = c.replace(old, new)

print("✅ TV repositioned in front of couch")

# ===== 2. FIX CAT SHAPE — proper feline body =====
old_cat = """function buildCat(scene,phys){
  const g=new THREE.Group();
  const fMat=new THREE.MeshStandardMaterial({color:0xe87840,roughness:.85});
  const bMat2=new THREE.MeshStandardMaterial({color:0xf0d0b0,roughness:.85});
  g.add(new THREE.Mesh(new THREE.CapsuleGeometry(.12,.2,6,8),fMat).position.set(0,.08,0));
  g.add(new THREE.Mesh(new THREE.SphereGeometry(.08,8,8),fMat).position.set(.18,.15,0));
  for(const sx of[-.04,.04]){
    g.add(new THREE.Mesh(new THREE.ConeGeometry(.03,.04,4),fMat).position.set(.18+sx,.22,0));
    g.add(new THREE.Mesh(new THREE.ConeGeometry(.015,.025,4),bMat2).position.set(.18+sx,.21,0));
  }
  const eMat2=new THREE.MeshStandardMaterial({color:0x44cc44,emissive:0x22aa22,emissiveIntensity:.3});
  for(const ex of[-.03,.03])
    g.add(new THREE.Mesh(new THREE.SphereGeometry(.02,6,6),eMat2).position.set(.2+ex,.16,.07));
  const tMat=new THREE.MeshStandardMaterial({color:0xe87840,roughness:.85});
  const tC=new THREE.CatmullRomCurve3([new THREE.Vector3(-.15,.04,0),new THREE.Vector3(-.22,.08,.02),new THREE.Vector3(-.26,.15,-.02),new THREE.Vector3(-.24,.2,.01)]);
  g.add(new THREE.Mesh(new THREE.TubeGeometry(tC,8,.01,4,false),tMat));
  g.position.set(-13,.02,10.5);g.rotation.y=-.5;scene.add(g);
  catNPC={mesh:g,pos:new THREE.Vector3(-13,.02,10.5),sleep:new THREE.Vector3(-13,.02,10.5),sleeping:true,awakeR:3.5,wT:0,state:'sleep',gT:0,eMat:eMat2};
  phys.add(new Body({pos:new THREE.Vector3(-13,.2,10.5),hs:new THREE.Vector3(.25,.15,.25),static:true,tag:'catC'}));
}"""

new_cat = """function buildCat(scene,phys){
  const g=new THREE.Group();
  const fMat=new THREE.MeshStandardMaterial({color:0xe87840,roughness:.85});
  const fMat2=new THREE.MeshStandardMaterial({color:0xcc6630,roughness:.85});
  const bMat2=new THREE.MeshStandardMaterial({color:0xf0d0b0,roughness:.85});
  const dMat=new THREE.MeshStandardMaterial({color:0x222222,roughness:.3});
  const nMat=new THREE.MeshStandardMaterial({color:0xffaaaa,roughness:.5});

  // Main body — elongated capsule
  const body=new THREE.Mesh(new THREE.CapsuleGeometry(0.1,0.25,6,8),fMat);
  body.position.y=0.08;body.rotation.z=Math.PI/2;body.rotation.y=Math.PI/2;body.castShadow=true;
  g.add(body);

  // Belly — lighter underside
  const belly=new THREE.Mesh(new THREE.SphereGeometry(0.07,6,6),bMat2);
  belly.scale.set(1.8,0.45,1);belly.position.set(0,0.02,0.04);
  g.add(belly);

  // Head — round with pointed chin
  const head=new THREE.Mesh(new THREE.SphereGeometry(0.07,8,8),fMat);
  head.position.set(0.18,0.14,0);head.scale.set(1,0.9,0.85);
  g.add(head);

  // Ears — triangular pointed
  for(const sx of[-0.03,0.03]){
    const earOuter=new THREE.Mesh(new THREE.ConeGeometry(0.025,0.035,4),fMat);
    earOuter.position.set(0.19+sx*0.9,0.21,0);
    earOuter.rotation.z=sx*0.3;
    g.add(earOuter);
    const earInner=new THREE.Mesh(new THREE.ConeGeometry(0.012,0.02,4),nMat);
    earInner.position.set(0.19+sx*0.9,0.205,0);
    earInner.rotation.z=sx*0.3;
    g.add(earInner);
  }

  // Eyes — almond shaped (elongated spheres)
  const eMat2=new THREE.MeshStandardMaterial({color:0x44cc44,emissive:0x22aa22,emissiveIntensity:0.4});
  for(const ex of[-0.025,0.025]){
    const eye=new THREE.Mesh(new THREE.SphereGeometry(0.018,6,6),eMat2);
    eye.position.set(0.21+ex*1.2,0.155,0.055);
    eye.scale.set(1.3,0.7,0.6);
    g.add(eye);
    // Pupil — vertical slit
    const pupil=new THREE.Mesh(new THREE.SphereGeometry(0.008,6,6),dMat);
    pupil.position.set(0.21+ex*1.2,0.153,0.062);
    pupil.scale.set(0.5,1.2,0.5);
    g.add(pupil);
  }

  // Nose — tiny pink triangle
  const nose=new THREE.Mesh(new THREE.ConeGeometry(0.005,0.005,4),nMat);
  nose.position.set(0.24,0.13,0.045);
  g.add(nose);

  // Whiskers
  const wMat=new THREE.LineBasicMaterial({color:0xffffff});
  for(const sx of[-1,1])for(let i=0;i<3;i++){
    const pts=[new THREE.Vector3(0.22,0.13+sx*0.005,0.05+i*0.01),
               new THREE.Vector3(0.22+0.05,0.12+sx*0.01,0.05+i*0.015)];
    g.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),wMat));
  }

  // Front legs — thicker at bottom (paws)
  for(const sx of[-0.06,0.06]){
    const leg=new THREE.Mesh(new THREE.CylinderGeometry(0.012,0.018,0.06,6),fMat);
    leg.position.set(sx,0.03,0.15);leg.castShadow=true;
    g.add(leg);
    const paw=new THREE.Mesh(new THREE.SphereGeometry(0.015,6,6),nMat);
    paw.position.set(sx,0.01,0.16);paw.scale.set(1,0.4,0.8);
    g.add(paw);
  }

  // Back legs
  for(const sx of[-0.06,0.06]){
    const leg=new THREE.Mesh(new THREE.CylinderGeometry(0.014,0.02,0.065,6),fMat);
    leg.position.set(sx,0.03,-0.12);leg.castShadow=true;
    g.add(leg);
    const paw=new THREE.Mesh(new THREE.SphereGeometry(0.015,6,6),nMat);
    paw.position.set(sx,0.01,-0.13);paw.scale.set(1,0.4,0.8);
    g.add(paw);
  }

  // Tail — long curved with fluffy tip
  const tailPts=[new THREE.Vector3(0,-0.02,-0.2),new THREE.Vector3(-0.04,0.04,-0.25),
                 new THREE.Vector3(-0.07,0.12,-0.22),new THREE.Vector3(-0.06,0.2,-0.18)];
  const tailCurve=new THREE.CatmullRomCurve3(tailPts);
  const tail=new THREE.Mesh(new THREE.TubeGeometry(tailCurve,10,0.008,5,false),fMat2);
  g.add(tail);

  // Fluffy tail tip
  const tip=new THREE.Mesh(new THREE.SphereGeometry(0.015,6,6),fMat2);
  tip.position.set(-0.06,0.2,-0.18);
  g.add(tip);

  g.position.set(-13,0.02,10.5);g.rotation.y=-0.5;g.scale.set(2.2,2.2,2.2);
  scene.add(g);

  catNPC={mesh:g,pos:new THREE.Vector3(-13,0.02,10.5),sleep:new THREE.Vector3(-13,0.02,10.5),sleeping:true,awakeR:3.5,wT:0,state:'sleep',gT:0,eMat:eMat2};
  phys.add(new Body({pos:new THREE.Vector3(-13,0.2,10.5),hs:new THREE.Vector3(0.3,0.15,0.3),static:true,tag:'catC'}));
}"""
c = c.replace(old_cat, new_cat)
print("✅ Cat shape rebuilt with proper feline anatomy")

# ===== 3. LOWER ROOM BARRIER DIFFICULTY - widen doorways =====
# Currently room dividers are impenetrable walls with small gaps
# Change to shorter walls with wider openings

# Living room ↔ Bedroom divider (x=-20 to 0 at z=-.15):
# Change from full wall to partial height + wider gap
old = "const lrDiv=new THREE.Mesh(new THREE.BoxGeometry(20,HH,wt),wallMat);lrDiv.position.set(-10,HH/2,-.15);lrDiv.castShadow=true;scene.add(lrDiv);allBuildingMeshes.push(lrDiv);addSB(20,HH,wt,-10,HH/2,-.15);"
# Split into two shorter sections with a door gap at x≈-6
new = "const lrDivL=new THREE.Mesh(new THREE.BoxGeometry(8,HH*0.6,wt),wallMat);lrDivL.position.set(-16,HH*0.3,-.15);lrDivL.castShadow=true;scene.add(lrDivL);allBuildingMeshes.push(lrDivL);addSB(8,HH*0.6,wt,-16,HH*0.3,-.15);const lrDivR=new THREE.Mesh(new THREE.BoxGeometry(8,HH*0.6,wt),wallMat);lrDivR.position.set(-2,HH*0.3,-.15);lrDivR.castShadow=true;scene.add(lrDivR);allBuildingMeshes.push(lrDivR);addSB(8,HH*0.6,wt,-2,HH*0.3,-.15);"
c = c.replace(old, new)

# Kitchen ↔ Bathroom divider (x=0 to 10 at z=-.15): same treatment
old = "const kbDiv=new THREE.Mesh(new THREE.BoxGeometry(10,HH,wt),wallMat);kbDiv.position.set(5,HH/2,-.15);kbDiv.castShadow=true;scene.add(kbDiv);allBuildingMeshes.push(kbDiv);addSB(10,HH,wt,5,HH/2,-.15);"
new = "const kbDivL=new THREE.Mesh(new THREE.BoxGeometry(4,HH*0.6,wt),wallMat);kbDivL.position.set(2,HH*0.3,-.15);kbDivL.castShadow=true;scene.add(kbDivL);allBuildingMeshes.push(kbDivL);addSB(4,HH*0.6,wt,2,HH*0.3,-.15);const kbDivR=new THREE.Mesh(new THREE.BoxGeometry(4,HH*0.6,wt),wallMat);kbDivR.position.set(8,HH*0.3,-.15);kbDivR.castShadow=true;scene.add(kbDivR);allBuildingMeshes.push(kbDivR);addSB(4,HH*0.6,wt,8,HH*0.3,-.15);"
c = c.replace(old, new)

# Playroom ↔ Bedroom divider: remove completely and replace with open archway
old = "const prDiv=new THREE.Mesh(new THREE.BoxGeometry(wt,HH,16),wallMat);prDiv.position.set(-19.85,HH/2,-8);prDiv.castShadow=true;scene.add(prDiv);allBuildingMeshes.push(prDiv);addSB(wt,HH,16,-19.85,HH/2,-8);"
new = "const prDiv=new THREE.Mesh(new THREE.BoxGeometry(wt,HH*0.4,8),wallMat);prDiv.position.set(-19.85,HH*0.2,-2);prDiv.castShadow=true;scene.add(prDiv);allBuildingMeshes.push(prDiv);addSB(wt,HH*0.4,8,-19.85,HH*0.2,-2);"
c = c.replace(old, new)

# Remove the unnecessary interior walls at x axis (the ones that block the main corridor)
old = "makeWall(mW2,rH,wt,wallMat,-mW2/2,rH/2,0);addSB(mW2,rH,wt,-mW2/2,rH/2,0);\n  makeWall(mW2-3"
# Remove the wall, keep the second one
new = "// removed interior wall\n  makeWall(mW2-3"
c = c.replace(old, new)

print("✅ Room barriers lowered — wider openings for exploration")

# ===== 4. INTERACTIVE FRONT DOOR =====
# Replace the front door mesh with an interactable version
# When clicked with 3 keys, door opens and game completes

# Find the current door creation and make it interactable
old_door = "const door=new THREE.Mesh(new THREE.BoxGeometry(3.5,6,.15),new THREE.MeshStandardMaterial({color:0x6a3a20,roughness:.7,metalness:.1}));\n  door.position.set(0,3,mD2+wt/2+.08);door.name='frontDoor';door.castShadow=true;scene.add(door);allBuildingMeshes.push(door);\n  addSB(1.75,3,.1,0,3,mD2+.2);"

new_door = """const door=new THREE.Mesh(new THREE.BoxGeometry(3.5,6,.15),new THREE.MeshStandardMaterial({color:0x6a3a20,roughness:.7,metalness:.1}));
  door.position.set(0,3,mD2+wt/2+.08);door.name='frontDoor';door.castShadow=true;scene.add(door);allBuildingMeshes.push(door);
  addSB(1.75,3,.1,0,3,mD2+.2);
  // Interactive front door — click to escape with all 3 keys
  const doorBody=new Body({pos:new THREE.Vector3(0,3,mD2+wt/2+.08),hs:new THREE.Vector3(1.75,3,.15),static:true,tag:'frontDoor',isInteractable:true,interactType:'activate',
    interactPrompt:GS.keysFound>=3?'🚪 Open the front door and ESCAPE!':'🔒 Locked — find 3 keys first ('+GS.keysFound+'/3)',
    data:{points:0}});
  phys.add(doorBody);
  registerInteractable(doorBody,'activate','Front door',()=>{
    if(GS.keysFound>=3&&!GS._escaped){
      GS._escaped=true;
      // Animate door opening
      door.rotation.y=-Math.PI/2;door.position.x=-0.5;
      sfxDoor();
      showToast('🎉 The door swings open! You escaped!','success');
      addScore(100,'Escaped the house! +100');
      setTimeout(()=>completeGame(),1500);
      burstSparkles(0,3,mD2+wt/2+.5,20);
    }else{
      showToast('🔒 The door is locked. Find all 3 keys first! ('+GS.keysFound+'/3)','');
      sfx(200,.15,'triangle',.03);
    }
  });"""

c = c.replace(old_door, new_door)
print("✅ Front door is now interactable — escape with 3 keys!")

# Also update the interact prompt for the door to show dynamic key count
# Fix the onInteract prompt in interactPrompt
c = c.replace(
    "interactPrompt:GS.keysFound>=3?'🚪 Open the front door and ESCAPE!':'🔒 Locked — find 3 keys first ('+GS.keysFound+'/3)'",
    "interactPrompt:GS.keysFound>=3?'🚪 Open the front door!':'🔒 Need '+GS.keysFound+'/3 keys'"
)

# Remove the old auto-escape detection (no longer needed, door handles it)
old_escape = """if(GS.quests.main.done&&!GS._escaped){const p=mouseBody.pos;if(p.distanceTo(new THREE.Vector3(0,0,14.5))<3){GS._escaped=true;completeGame();}}"""
new_escape = """// Door escape now handled by front door interaction"""
c = c.replace(old_escape, new_escape)
print("✅ Auto-escape replaced with interactive door escape")

# ===== 5. QUEST GUIDANCE SYSTEM =====
# Add an interactive quest guidance overlay that shows what to do next
# Add quest arrow/waypoint marker system

guidance_js = """
/* --- QUEST GUIDANCE SYSTEM --- */
const QUEST_GUIDES = {
  main: [
    { hint: 'Talk to Woody in the living room — he knows where keys are!', room: 'Living Room', pos: [-15, 0.5, 8] },
    { hint: 'Find the cookie jar in the kitchen — something shiny is inside!', room: 'Kitchen', pos: [9, 0.5, 2] },
    { hint: 'Look under the bed in the bedroom — something glints!', room: 'Bedroom', pos: [-14, 0.5, -4] },
    { hint: 'Check behind the mirror in the hallway!', room: 'Hallway', pos: [16, 0.5, -14] },
  ],
  toy: { hint: 'Head to the living room and open the toy box!', pos: [-17, 0.5, 9] },
  plant: { hint: 'Find the watering can in the hallway!', pos: [14, 0.5, -10] },
  faucet: { hint: 'Go to the bathroom and turn off the faucet!', pos: [1.5, 0.5, -20] },
  cabinet: { hint: 'The playroom cabinet has a 3-digit code. Check the blue book on the bookshelf!', pos: [-25, 0.5, -1] },
  attic: { hint: 'Climb the ladder in the bedroom to reach the attic!', pos: [-18, 0.5, -3] },
  toys: { hint: 'Find and talk to all 4 toy characters around the house!', pos: [0, 0.5, 0] },
  clock: { hint: 'Find the grandfather clock in the hallway and wind it!', pos: [12, 0.5, 2] },
};

function getActiveQuestGuide() {
  const q = GS.quests;
  if (!q.main.done) return { id: 'main', ...QUEST_GUIDES.main[Math.min(GS.keysFound, QUEST_GUIDES.main.length-1)] };
  if (!q.toys.done) return { id: 'toys', ...QUEST_GUIDES.toy };
  if (!q.toy.done) return { id: 'toy', ...QUEST_GUIDES.toy };
  if (!q.plant.done) return { id: 'plant', ...QUEST_GUIDES.plant };
  if (!q.faucet.done) return { id: 'faucet', ...QUEST_GUIDES.faucet };
  if (!q.cabinet.done) return { id: 'cabinet', ...QUEST_GUIDES.cabinet };
  if (!q.clock.done) return { id: 'clock', ...QUEST_GUIDES.clock };
  if (!q.attic.done) return { id: 'attic', ...QUEST_GUIDES.attic };
  return null;
}

let guideArrow = null;
let guideLabel = null;

function buildQuestGuide(scene) {
  // Create waypoint marker
  const arrowMat = new THREE.MeshBasicMaterial({ color: 0xf0a030, transparent: true, opacity: 0.6 });
  const arrow = new THREE.Mesh(new THREE.ConeGeometry(0.15, 0.3, 6), arrowMat);
  arrow.position.y = 2.5;
  arrow.visible = false;
  scene.add(arrow);
  guideArrow = arrow;

  // Create floating waypoint label billboard
  const canvas = document.createElement('canvas');
  canvas.width = 256; canvas.height = 64;
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = 'rgba(0,0,0,0)';
  ctx.fillRect(0, 0, 256, 64);
  const tex = new THREE.CanvasTexture(canvas);
  tex.needsUpdate = true;
  const spriteMat = new THREE.SpriteMaterial({ map: tex, transparent: true, opacity: 0.9, depthTest: false });
  const sprite = new THREE.Sprite(spriteMat);
  sprite.position.y = 3.5;
  sprite.scale.set(1.5, 0.4, 1);
  sprite.visible = false;
  scene.add(sprite);
  guideLabel = { sprite, tex, ctx, canvas };
}

function updateQuestGuide(dt, playerPos) {
  if (!guideArrow || !guideLabel) return;

  const guide = getActiveQuestGuide();
  if (!guide || !guide.pos) {
    guideArrow.visible = false;
    guideLabel.sprite.visible = false;
    return;
  }

  const [tx, ty, tz] = guide.pos;
  const target = new THREE.Vector3(tx, ty, tz);
  const dist = playerPos.distanceTo(target);

  // Don't show waypoint if already at the target
  if (dist < 3) {
    guideArrow.visible = false;
    guideLabel.sprite.visible = false;
    return;
  }

  // Show floating arrow pointing toward target
  guideArrow.visible = true;
  guideArrow.position.copy(playerPos);
  guideArrow.position.y = 2.0;

  const dx = tx - playerPos.x;
  const dz = tz - playerPos.z;
  guideArrow.rotation.y = Math.atan2(dx, dz) + Math.PI;

  // Bob the arrow
  guideArrow.position.y += Math.sin(performance.now() * 0.003) * 0.1;

  // Show floating label
  guideLabel.sprite.visible = true;

  // Update label text
  const canvas = guideLabel.canvas;
  const ctx = guideLabel.ctx;
  ctx.clearRect(0, 0, 256, 64);

  // Background
  ctx.fillStyle = 'rgba(15, 12, 18, 0.75)';
  ctx.beginPath();
  ctx.roundRect(10, 5, 236, 54, 12);
  ctx.fill();

  // Border
  ctx.strokeStyle = '#f0a030';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.roundRect(10, 5, 236, 54, 12);
  ctx.stroke();

  // Text
  ctx.fillStyle = '#f0e8d8';
  ctx.font = 'bold 18px Fredoka, sans-serif';
  ctx.fillText('🎯 ' + (guide.hint || 'Go here!'), 20, 40);

  guideLabel.tex.needsUpdate = true;

  // Position the label at target
  guideLabel.sprite.position.set(tx, 4.0, tz);
}

// Add roundRect polyfill for canvas if needed
if (!CanvasRenderingContext2D.prototype.roundRect) {
  CanvasRenderingContext2D.prototype.roundRect = function(x, y, w, h, r) {
    if (r > w/2) r = w/2;
    if (r > h/2) r = h/2;
    this.moveTo(x + r, y);
    this.lineTo(x + w - r, y);
    this.quadraticCurveTo(x + w, y, x + w, y + r);
    this.lineTo(x + w, y + h - r);
    this.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    this.lineTo(x + r, y + h);
    this.quadraticCurveTo(x, y + h, x, y + h - r);
    this.lineTo(x, y + r);
    this.quadraticCurveTo(x, y, x + r, y);
    this.closePath();
  };
}
"""

# Insert guidance JS before the init block
c = c.replace(
    "/* ---------- INIT ---------- */",
    guidance_js + "\n\n/* ---------- INIT ---------- */"
)

# Add buildQuestGuide call to init
c = c.replace(
    "buildLightRays(scene);buildToyNPCs(scene,phys);buildVacuum(scene,phys);buildCat(scene,phys);buildClock(scene,phys);",
    "buildLightRays(scene);buildToyNPCs(scene,phys);buildVacuum(scene,phys);buildCat(scene,phys);buildClock(scene,phys);\n    buildQuestGuide(scene);"
)

# Add updateQuestGuide to loop
c = c.replace(
    "updateClock(dt);\n  composer.render();",
    "updateClock(dt);\n  updateQuestGuide(dt,mouseBody.pos);\n  composer.render();"
)

# Remove the old "Auto-escape now handled" placeholder line
c = c.replace("""// Door escape now handled by front door interaction""", "")

print("✅ Quest guidance system added — waypoint arrows show where to go")

# Also fix the new_escape removal that left a blank line
c = c.replace("""  \n  if(!GS.quests.attic.done""", """  if(!GS.quests.attic.done""")

# Write output
with open(PATH, 'w') as f:
    f.write(c)

import os
orig_size = os.path.getsize(BAK)
new_size = len(c)
print(f"\n✅ ALL 5 FIXES APPLIED!")
print(f"📏 {orig_size} → {new_size} bytes ({new_size - orig_size:+d})")
print(f"📁 {PATH}")
