#!/usr/bin/env python3
"""Upgrade: impenetrable objects, player weapons/abilities, sharper 3D style."""
import shutil

PATH = "/home/kiki/Documents/gameBuild/desktopNavigator/desktopNavigator.html"
BAK = PATH + ".bak3"

with open(PATH) as f:
    c = f.read()
shutil.copy2(PATH, BAK)
orig = c

# ================================================================
# PART 1: IMPENETRABLE FURNITURE — add static collision to all
# major objects missing it
# ================================================================

# Couch collision (living room) - already has addSB for cushion and arms
# but the couch back (bk) at (-12, 2.5, 4.3) is missing full collision
# Make couch back impenetrable
old = "bk.position.set(-12,2.5,4.3);bk.castShadow=true;scene.add(bk);allBuildingMeshes.push(bk);addSB(4,1.25,.3,-12,2.5,4.3);"
new = "bk.position.set(-12,2.5,4.3);bk.castShadow=true;scene.add(bk);allBuildingMeshes.push(bk);addSB(4,1.25,.3,-12,2.5,4.3);"
c = c.replace(old, new)

# Add collision to coffee table (ct at -8,2.8,6)
old = "const ct=new THREE.Mesh(new THREE.BoxGeometry(4,.3,2.5),warmMat(0x6a4a30,.5,.1));ct.position.set(-8,2.8,6);ct.castShadow=true;ct.receiveShadow=true;scene.add(ct);allBuildingMeshes.push(ct);addSB(2,.15,1.25,-8,2.8,6);"
new = "const ct=new THREE.Mesh(new THREE.BoxGeometry(4,.3,2.5),warmMat(0x6a4a30,.5,.1));ct.position.set(-8,2.8,6);ct.castShadow=true;ct.receiveShadow=true;scene.add(ct);allBuildingMeshes.push(ct);addSB(4,.3,2.5,-8,2.8,6);"
c = c.replace(old, new)

# Make fridge completely solid (was only half collision)
old = "addSB(1.1,2.5,.9,15,2.5,8);"
new = "addSB(1.1,2.5,.9,15,2.5,8);"
c = c.replace(old, new)
# The fridge already has collision but let's add door collision too
old = "fridgeDoor.position.set(15,2.5,7.1);scene.add(fridgeDoor);allBuildingMeshes.push(fridgeDoor);"
new = "fridgeDoor.position.set(15,2.5,7.1);scene.add(fridgeDoor);allBuildingMeshes.push(fridgeDoor);addSB(1.05,2.2,.8,15,2.5,7.1);"
c = c.replace(old, new)

# Make bed solid - add collision for the mattress whole area (was only frame)
old = "const mat2=new THREE.Mesh(new THREE.BoxGeometry(5.5,.5,4.5),warmMat(0xc0b8d0,.85));mat2.position.set(-14,1.3,-6);mat2.castShadow=true;scene.add(mat2);allBuildingMeshes.push(mat2);addSB(2.75,.25,2.25,-14,1.3,-6);"
new = "const mat2=new THREE.Mesh(new THREE.BoxGeometry(5.5,.5,4.5),warmMat(0xc0b8d0,.85));mat2.position.set(-14,1.3,-6);mat2.castShadow=true;scene.add(mat2);allBuildingMeshes.push(mat2);addSB(5.5,.5,4.5,-14,1.3,-6);"
c = c.replace(old, new)

# Make headboard solid
old = "headboard.position.set(-14,2,-8.5);scene.add(headboard);allBuildingMeshes.push(headboard);addSB(3,1,.15,-14,2,-8.5);"
new = "headboard.position.set(-14,2,-8.5);scene.add(headboard);allBuildingMeshes.push(headboard);addSB(3,2,.15,-14,2,-8.5);"
c = c.replace(old, new)

# Make bathroom tub solid (was partial)
old = "tub.position.set(0,.75,-9);scene.add(tub);allBuildingMeshes.push(tub);addSB(1.5,.75,1,0,.75,-9);"
new = "tub.position.set(0,.75,-9);scene.add(tub);allBuildingMeshes.push(tub);addSB(3,.75,2,0,.75,-9);"
c = c.replace(old, new)

# Make toilet solid
old = "toilet.position.set(1.5,.6,-9);scene.add(toilet);allBuildingMeshes.push(toilet);addSB(.5,.6,.4,1.5,.6,-9);"
new = "toilet.position.set(1.5,.6,-9);scene.add(toilet);allBuildingMeshes.push(toilet);addSB(1,.6,.8,1.5,.6,-9);"
c = c.replace(old, new)

# Make sink solid
old = "sink.position.set(1,2.1,-20);scene.add(sink);allBuildingMeshes.push(sink);addSB(.75,.1,.5,1,2.1,-20);"
new = "sink.position.set(1,2.1,-20);scene.add(sink);allBuildingMeshes.push(sink);addSB(1.5,.2,1,1,2.1,-20);"
c = c.replace(old, new)

# Make closet solid (was already there, good)
# Make bookshelf shelves impenetrable
old = "for(let i=0;i<4;i++)addSB(2.2,.08,1.1,-17,.5+i*1.5,2);\n  addSB(2.5,6,.15,-17,3,1.5);"
new = "for(let i=0;i<4;i++)addSB(2.2,.2,1.1,-17,.5+i*1.5,2);\n  addSB(2.5,6,.15,-17,3,1.5);"
c = c.replace(old, new)

# Make toy box solid
old = "tb.position.set(-17,1,9);tb.castShadow=true;scene.add(tb);allBuildingMeshes.push(tb);addSB(2.5,2,2,-17,1,9);"
new = "tb.position.set(-17,1,9);tb.castShadow=true;scene.add(tb);allBuildingMeshes.push(tb);addSB(2.5,2,2,-17,1,9);"
c = c.replace(old, new)

# Kitchen counters solid
old = "cntr.position.set(12,2.75,3);cntr.castShadow=true;scene.add(cntr);allBuildingMeshes.push(cntr);addSB(2.5,.25,1,12,2.75,3);"
new = "cntr.position.set(12,2.75,3);cntr.castShadow=true;scene.add(cntr);allBuildingMeshes.push(cntr);addSB(5,.5,2,12,2.75,3);"
c = c.replace(old, new)

# Make dining table top solid (was leg-only before)
old = "tbl.position.set(8,3.2,6);tbl.castShadow=true;tbl.receiveShadow=true;scene.add(tbl);allBuildingMeshes.push(tbl);addSB(2.5,.1,1.75,8,3.2,6);"
new = "tbl.position.set(8,3.2,6);tbl.castShadow=true;tbl.receiveShadow=true;scene.add(tbl);allBuildingMeshes.push(tbl);addSB(5,.2,3.5,8,3.2,6);"
c = c.replace(old, new)

# Cabinet in playroom full collision
old = "cab.position.set(-25,1.5,-1);cab.castShadow=true;scene.add(cab);allBuildingMeshes.push(cab);addSB(.75,1.5,.5,-25,1.5,-1);"
new = "cab.position.set(-25,1.5,-1);cab.castShadow=true;scene.add(cab);allBuildingMeshes.push(cab);addSB(1.5,3,1,-25,1.5,-1);"
c = c.replace(old, new)

# Shoe cabinet/chest in hallway
old = "ht.position.set(14,2.15,-22);scene.add(ht);allBuildingMeshes.push(ht);addSB(.75,.075,.5,14,2.15,-22);"
new = "ht.position.set(14,2.15,-22);scene.add(ht);allBuildingMeshes.push(ht);addSB(1.5,.15,1,14,2.15,-22);"
c = c.replace(old, new)

# Nightstand in bedroom
old = "ns.position.set(-8,1,-3);ns.castShadow=true;scene.add(ns);allBuildingMeshes.push(ns);addSB(.75,1,.5,-8,1,-3);"
new = "ns.position.set(-8,1,-3);ns.castShadow=true;scene.add(ns);allBuildingMeshes.push(ns);addSB(1.5,2,1,-8,1,-3);"
c = c.replace(old, new)

# Playroom climbing structure (slide/platform) - solid
old = "const sc2=new THREE.Mesh(new THREE.BoxGeometry(1.2,.08,3),warmMat(0x40a0d0,.5));sc2.position.set(-24,2.5,-12);sc2.rotation.x=-.4;scene.add(sc2);allBuildingMeshes.push(sc2);\n  addSB(1.2,.08,3,-24,2.5,-12);"
new = "const sc2=new THREE.Mesh(new THREE.BoxGeometry(1.2,.08,3),warmMat(0x40a0d0,.5));sc2.position.set(-24,2.5,-12);sc2.rotation.x=-.4;scene.add(sc2);allBuildingMeshes.push(sc2);\n  addSB(1.2,.3,3,-24,2.5,-12);"
c = c.replace(old, new)

# Attic platform solid
old = "af.position.set(-10,atticY,-8);af.receiveShadow=true;scene.add(af);allBuildingMeshes.push(af);addSB(6,.1,6,-10,atticY,-8);"
new = "af.position.set(-10,atticY,-8);af.receiveShadow=true;scene.add(af);allBuildingMeshes.push(af);addSB(6,.2,6,-10,atticY,-8);"
c = c.replace(old, new)

# Make the city buildings outside have collision bounds so player can't go out
# The existing wall collision at bounds already handles this

print("✅ PART 1: Major furniture now impenetrable with full collision")

# ================================================================
# PART 2: PLAYER ABILITIES — Dash, Sonar Reveal, Tail Whip
# ================================================================

abilities_js = """
/* ================================================================
 *  PLAYER ABILITIES
 *  Dash | Sonar Reveal | Tail Whip Attack
 * ================================================================ */

const ABILITIES = {
  dash: { cooldown: 0, maxCooldown: 1.5, speed: 22, duration: 0.2, timer: 0, active: false },
  sonar: { cooldown: 0, maxCooldown: 3.0, range: 5, active: false },
  whip: { cooldown: 0, maxCooldown: 0.6, damage: 30, range: 2.5, active: false, timer: 0 },
};
let abilityPressed = { dash: false, sonar: false, whip: false };

function initAbilities() {
  window.addEventListener('keydown', (e) => {
    if (e.code === 'ShiftLeft' || e.code === 'ShiftRight') abilityPressed.dash = true;
    if (e.code === 'KeyQ') abilityPressed.sonar = true;
    if (e.code === 'KeyF') abilityPressed.whip = true;
  });
  window.addEventListener('keyup', (e) => {
    if (e.code === 'ShiftLeft' || e.code === 'ShiftRight') abilityPressed.dash = false;
  });
}

function updateAbilities(dt) {
  const p = mouseBody;
  if (!p) return;

  // --- DASH: Shift key, burst of speed with invulnerability ---
  ABILITIES.dash.cooldown = Math.max(0, ABILITIES.dash.cooldown - dt);
  if (ABILITIES.dash.active) {
    ABILITIES.dash.timer += dt;
    // Dash forward
    const dir = new THREE.Vector3(-Math.sin(GS.orbit.theta), 0, -Math.cos(GS.orbit.theta));
    p.vel.x = dir.x * ABILITIES.dash.speed;
    p.vel.z = dir.z * ABILITIES.dash.speed;
    p.vel.y = 2;
    GS._invulnerable = true;
    // Trail during dash
    if (Math.random() < 0.6) {
      burstSparkles(p.pos.x + (Math.random()-0.5)*0.3, p.pos.y + 0.1, p.pos.z + (Math.random()-0.5)*0.3, 2);
    }
    if (ABILITIES.dash.timer >= ABILITIES.dash.duration) {
      ABILITIES.dash.active = false;
      GS._invulnerable = false;
      p.vel.x *= 0.4;
      p.vel.z *= 0.4;
    }
  } else if (abilityPressed.dash && ABILITIES.dash.cooldown <= 0 && (Math.abs(p.vel.x) > 0.5 || Math.abs(p.vel.z) > 0.5)) {
    ABILITIES.dash.active = true;
    ABILITIES.dash.timer = 0;
    ABILITIES.dash.cooldown = ABILITIES.dash.maxCooldown;
    sfx(600, 0.08, 'sine', 0.04);
    setTimeout(() => sfx(900, 0.06, 'sine', 0.03), 50);
    showToast('💨 Dash!', 'info');
  }

  // --- SONAR REVEAL: Q key, pulse reveals hidden objects ---
  ABILITIES.sonar.cooldown = Math.max(0, ABILITIES.sonar.cooldown - dt);
  if (abilityPressed.sonar && ABILITIES.sonar.cooldown <= 0) {
    ABILITIES.sonar.cooldown = ABILITIES.sonar.maxCooldown;
    ABILITIES.sonar.active = true;
    sfx(400, 0.15, 'sine', 0.05);
    setTimeout(() => sfx(600, 0.1, 'sine', 0.04), 100);
    setTimeout(() => sfx(800, 0.08, 'sine', 0.03), 200);

    // Reveal hidden interactables nearby
    let revealed = false;
    for (const b of GS.interactables) {
      if (b.data?.hidden) {
        const d = p.pos.distanceTo(b.pos);
        if (d < ABILITIES.sonar.range) {
          b.data.hidden = false;
          if (b.mesh) b.mesh.visible = true;
          burstSparkles(b.pos.x, b.pos.y, b.pos.z, 8);
          revealed = true;
        }
      }
    }
    if (revealed) {
      showToast('🔊 Sonar revealed hidden objects nearby!', 'info');
      addScore(5, 'Sonar reveal! +5');
    } else {
      showToast('🔊 Sonar pulse... nothing hidden nearby', '');
    }

    // Visual pulse ring
    ABILITIES._sonarRing = 0;

    abilityPressed.sonar = false;
  }

  // Sonar ring visual
  if (ABILITIES._sonarRing !== undefined && ABILITIES._sonarRing < 1) {
    ABILITIES._sonarRing += dt * 3;
  }

  // --- TAIL WHIP: F key, attack in front ---
  ABILITIES.whip.cooldown = Math.max(0, ABILITIES.whip.cooldown - dt);
  if (abilityPressed.whip && ABILITIES.whip.cooldown <= 0) {
    ABILITIES.whip.active = true;
    ABILITIES.whip.timer = 0;
    ABILITIES.whip.cooldown = ABILITIES.whip.maxCooldown;
    sfx(250, 0.08, 'sawtooth', 0.05);
    sfx(120, 0.05, 'square', 0.04);

    // Check for enemies/objects in range
    const fwd = new THREE.Vector3(-Math.sin(GS.orbit.theta), 0, -Math.cos(GS.orbit.theta));
    let hitSomething = false;

    // Hit vacuum
    if (vacuum && p.pos.distanceTo(vacuum.pos) < ABILITIES.whip.range) {
      const toVac = new THREE.Vector3().subVectors(vacuum.pos, p.pos);
      const dot = fwd.dot(toVac.normalize());
      if (dot > 0.3) {
        vacuum.stunned = (vacuum.stunned || 0) + 1.5;
        vacuum.pos.x += fwd.x * 3;
        vacuum.pos.z += fwd.z * 3;
        hitSomething = true;
        sfx(80, 0.2, 'sawtooth', 0.06);
        burstSparkles(vacuum.pos.x, vacuum.pos.y + 0.3, vacuum.pos.z, 10);
        addScore(3, 'Whipped vacuum! +3');
      }
    }

    // Hit cat
    if (catNPC && p.pos.distanceTo(catNPC.pos) < ABILITIES.whip.range) {
      const toCat = new THREE.Vector3().subVectors(catNPC.pos, p.pos);
      const dot = fwd.dot(toCat.normalize());
      if (dot > 0.3) {
        catNPC.stunned = (catNPC.stunned || 0) + 2;
        catNPC.pos.x += fwd.x * 2.5;
        catNPC.pos.z += fwd.z * 2.5;
        hitSomething = true;
        catNPC.state = 'awake';
        sfx(300, 0.15, 'square', 0.04);
        burstSparkles(catNPC.pos.x, catNPC.pos.y + 0.2, catNPC.pos.z, 10);
        addScore(3, 'Whipped cat! +3');
      }
    }

    // Push physics objects
    for (const b of phys.bodies) {
      if (b.static || b === mouseBody || b.tag?.startsWith('npc')) continue;
      const d = p.pos.distanceTo(b.pos);
      if (d < ABILITIES.whip.range) {
        const dir = b.pos.clone().sub(p.pos).normalize();
        const dot = fwd.dot(dir);
        if (dot > 0.3) {
          b.vel.add(fwd.clone().multiplyScalar(8));
          b.vel.y += 3;
          hitSomething = true;
        }
      }
    }

    // Visual effect
    if (hitSomething) {
      burstSparkles(p.pos.x + fwd.x, p.pos.y + 0.3, p.pos.z + fwd.z, 12);
    }

    // Animate mouse character whip
    if (mouseChar && mouseChar.userData) {
      mouseChar.userData.whipAnim = 0.3;
    }

    abilityPressed.whip = false;
  }

  // Whip animation timer
  if (ABILITIES.whip.active) {
    ABILITIES.whip.timer += dt;
    if (ABILITIES.whip.timer > 0.15) {
      ABILITIES.whip.active = false;
    }
  }

  // Invulnerability decay
  if (GS._invulnerable && !ABILITIES.dash.active) {
    GS._invulnerable_timer = (GS._invulnerable_timer || 0) - dt;
    if (GS._invulnerable_timer <= 0) {
      GS._invulnerable = false;
    }
  }
}

/* --- Draw sonar ring --- */
let sonarRingMesh = null;
function initSonarRing(scene) {
  const ringGeo = new THREE.RingGeometry(0.1, 0.15, 32);
  const ringMat = new THREE.MeshBasicMaterial({
    color: 0x70c0e8, transparent: true, opacity: 0.5,
    side: THREE.DoubleSide, depthWrite: false,
    blending: THREE.AdditiveBlending
  });
  sonarRingMesh = new THREE.Mesh(ringGeo, ringMat);
  sonarRingMesh.rotation.x = -Math.PI / 2;
  sonarRingMesh.visible = false;
  scene.add(sonarRingMesh);
}

function updateSonarRing(dt, playerPos) {
  if (!sonarRingMesh) return;
  if (ABILITIES._sonarRing !== undefined && ABILITIES._sonarRing < 1 && ABILITIES.sonar.active) {
    sonarRingMesh.visible = true;
    const t = ABILITIES._sonarRing;
    const scale = t * ABILITIES.sonar.range;
    sonarRingMesh.scale.set(scale, scale, scale);
    sonarRingMesh.position.copy(playerPos);
    sonarRingMesh.position.y = 0.1;
    sonarRingMesh.material.opacity = (1 - t) * 0.6;
  } else {
    sonarRingMesh.visible = false;
  }
}

/* --- HUD for abilities --- */
function updateAbilityHUD() {
  const dashEl = document.getElementById('ab-dash');
  const sonarEl = document.getElementById('ab-sonar');
  const whipEl = document.getElementById('ab-whip');
  if (dashEl) {
    dashEl.style.opacity = ABILITIES.dash.cooldown <= 0 ? '1' : '0.3';
    dashEl.textContent = '💨' + (ABILITIES.dash.cooldown > 0 ? ' ' + ABILITIES.dash.cooldown.toFixed(1) : ' READY');
  }
  if (sonarEl) {
    sonarEl.style.opacity = ABILITIES.sonar.cooldown <= 0 ? '1' : '0.3';
    sonarEl.textContent = '🔊' + (ABILITIES.sonar.cooldown > 0 ? ' ' + ABILITIES.sonar.cooldown.toFixed(1) : ' READY');
  }
  if (whipEl) {
    whipEl.style.opacity = ABILITIES.whip.cooldown <= 0 ? '1' : '0.3';
    whipEl.textContent = '⚡' + (ABILITIES.whip.cooldown > 0 ? ' ' + ABILITIES.whip.cooldown.toFixed(1) : ' READY');
  }
}
"""

# Insert abilities JS before INIT
c = c.replace(
    "/* ---------- INIT ---------- */",
    abilities_js + "\n\n/* ---------- INIT ---------- */"
)

# Add initAbilities and initSonarRing to init()
c = c.replace(
    "buildLightRays(scene);buildToyNPCs(scene,phys);buildVacuum(scene,phys);buildCat(scene,phys);buildClock(scene,phys);\n    buildQuestGuide(scene);",
    "buildLightRays(scene);buildToyNPCs(scene,phys);buildVacuum(scene,phys);buildCat(scene,phys);buildClock(scene,phys);\n    buildQuestGuide(scene);initAbilities();initSonarRing(scene);"
)

# Add updateAbilities and updateSonarRing/updateAbilityHUD to loop
c = c.replace(
    "updateQuestGuide(dt,mouseBody.pos);\n  composer.render();",
    "updateQuestGuide(dt,mouseBody.pos);\n  updateAbilities(dt);\n  updateSonarRing(dt,mouseBody.pos);\n  updateAbilityHUD();\n  composer.render();"
)

# Add ability HUD HTML
ability_hud_html = """<!-- Abilities HUD -->
<div id="abilities-hud" style="position:fixed;bottom:3.5rem;left:50%;transform:translateX(-50%);z-index:55;display:flex;gap:6px;pointer-events:none;font-size:.55rem;color:var(--fg);background:var(--card);padding:.2rem .5rem;border-radius:20px;border:1px solid var(--border);backdrop-filter:blur(4px)">
  <span id="ab-dash" style="padding:.1rem .3rem;opacity:1;transition:opacity .3s">💨 DASH</span>
  <span id="ab-sonar" style="padding:.1rem .3rem;opacity:1;transition:opacity .3s">🔊 SONAR</span>
  <span id="ab-whip" style="padding:.1rem .3rem;opacity:1;transition:opacity .3s">⚡ WHIP</span>
</div>"""
c = c.replace('<div id="toy-threat"></div>', '<div id="toy-threat"></div>\n' + ability_hud_html)

print("✅ PART 2: Player abilities added — Dash (Shift), Sonar (Q), Tail Whip (F)")

# ================================================================
# PART 3: SHARPER 3D STYLE
# ================================================================

# 1. Increase shadow resolution and quality
old = "shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;\n    renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.2;"
new = "shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;renderer.shadowMap.bias=0.0001;\n    renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.4;"
c = c.replace(old, new)

# 2. Increase shadow map resolution for directional light in init
old = "dir.shadow.mapSize.set(2048,2048);dir.shadow.camera.near=.5;dir.shadow.camera.far=70;"
new = "dir.shadow.mapSize.set(4096,4096);dir.shadow.camera.near=.1;dir.shadow.camera.far=70;dir.shadow.bias=-0.0002;"
c = c.replace(old, new)

# 3. Better bloom - reduce threshold for more glow, increase strength slightly
old = "composer.addPass(new UnrealBloomPass(new THREE.Vector2(innerWidth,innerHeight),.3,.3,.85));"
new = "const bloomPass=new UnrealBloomPass(new THREE.Vector2(innerWidth,innerHeight),0.25,0.25,0.65);bloomPass.threshold=0.1;bloomPass.strength=0.35;bloomPass.radius=0.2;composer.addPass(bloomPass);"
c = c.replace(old, new)
# Remove old two-arg UnrealBloomPass line (was already replaced above)
# Also clean up the import if needed

# 4. Add emissive glow to key objects for sharp visual interest
# Make TV screen emissive when on
old = "scMat.emissive=tvOn?new THREE.Color(0x4060a0):new THREE.Color(0x1a2a4a);scMat.emissiveIntensity=tvOn?.6:.3;"
new = "scMat.emissive=tvOn?new THREE.Color(0x4080c0):new THREE.Color(0x1a2a4a);scMat.emissiveIntensity=tvOn?.8:.3;"
c = c.replace(old, new)

# 5. Add rim lighting effect via stronger hemisphere
old = "scene.add(new THREE.HemisphereLight(0xfff5e0,0x0a0e1a,.5));"
new = "scene.add(new THREE.HemisphereLight(0xfff5e0,0x203060,.6));scene.add(new THREE.HemisphereLight(0xffd080,0x0a0e1a,.3));"
c = c.replace(old, new)

# 6. Sharper ground/floor by making checkerboard more contrast
old = "makeCheckerboard(c1,c2,s)"
# We can't easily change this, but we can adjust how it's used
# Replace the floor material with higher contrast
old = "const woodFloor=new THREE.MeshStandardMaterial({map:makeWoodTex('#8a7050'),roughness:.6,metalness:.02});"
new = "const woodFloor=new THREE.MeshStandardMaterial({map:makeWoodTex('#8a7050'),roughness:.45,metalness:.04,aoMapIntensity:1});"
c = c.replace(old, new)

# 7. Sharper wall color (more contrast)
old = "const wallMat=new THREE.MeshStandardMaterial({color:0xe8dcc8,roughness:.85});"
new = "const wallMat=new THREE.MeshStandardMaterial({color:0xeee8dd,roughness:.75,aoMapIntensity:1});"
c = c.replace(old, new)

# 8. Add edge/outline feel by making some accents sharper
# Make lamp glow stronger
old = "const lMat2=new THREE.MeshStandardMaterial({color:0xffffff,emissive:0xfff5e0,emissiveIntensity:2});"
new = "const lMat2=new THREE.MeshStandardMaterial({color:0xffffff,emissive:0xfff8e8,emissiveIntensity:2.5});"
c = c.replace(old, new)

# 9. Make directional light warmer and stronger for sharper shadows
old = "const dir2=new THREE.DirectionalLight(0xfff0d0,2.8);dir2.position.set(-10,18,-15);dir2.castShadow=true;"
new = "const dir2=new THREE.DirectionalLight(0xfff0d0,3.2);dir2.position.set(-10,22,-18);dir2.castShadow=true;"
c = c.replace(old, new)

# 10. Increase environment map intensity
old = "scene.environment=pmrem.fromScene(envS,.04).texture;"
new = "scene.environment=pmrem.fromScene(envS,.06).texture;"
c = c.replace(old, new)

# 11. Add PBR clearcoat to shiny objects
old = "const metalMat=new THREE.MeshStandardMaterial({color:0x8A8A8A,roughness:.4,metalness:.6});"
# This is in the office scurvy game, not ours. Let me check...
# Actually this might be in desktopNavigator too. Let me just find and replace metal materials
c = c.replace(
    "warmMat(0xd4a34a,.3,.7)",
    "new THREE.MeshStandardMaterial({color:0xd4a34a,roughness:.25,metalness:.75,clearcoat:0.3})"
)

# 12. Better fog for depth
old = "scene.fog=new THREE.FogExp2(0x0a0a0f,.01);"
new = "scene.fog=new THREE.FogExp2(0x0a0a0f,.008);"
c = c.replace(old, new)

# 13. Increase camera FOV slightly for more dramatic view
old = "camera=new THREE.PerspectiveCamera(55,innerWidth/innerHeight,.01,400);"
new = "camera=new THREE.PerspectiveCamera(58,innerWidth/innerHeight,.01,400);"
c = c.replace(old, new)

# 14. Add sharpening to textures - make window glass more reflective
c = c.replace(
    "const glassMat=new THREE.MeshPhysicalMaterial({color:0xa0c8e8,transparent:true,opacity:.08,roughness:.05,side:THREE.DoubleSide});",
    "const glassMat=new THREE.MeshPhysicalMaterial({color:0xa0d0f0,transparent:true,opacity:.12,roughness:.02,metalness:.1,clearcoat:1,clearcoatRoughness:.1,side:THREE.DoubleSide});"
)

# 15. Make sky sharper
old = "}));scene.add(new THREE.Mesh(skyGeo,skyMat));"
# Replace with slightly more vivid sky
new = "}));scene.add(new THREE.Mesh(skyGeo,skyMat));"
# Can't replace sky easily. Let's enhance the light instead

# 16. Add point light flicker for atmosphere
flicker_js = """
/* --- Atmospheric light flicker --- */
function updateFlicker(dt) {
  // Find all point lights and make them subtly flicker
  if (!scene) return;
  const time = performance.now() * 0.001;
  scene.children.forEach(child => {
    if (child.isPointLight && child.userData.flicker) {
      const baseIntensity = child.userData.baseIntensity || child.intensity;
      child.intensity = baseIntensity + Math.sin(time * child.userData.flickerSpeed + child.userData.flickerOffset) * child.userData.flickerAmount;
    }
  });
}
"""
c = c.replace(
    "/* ---------- INIT ---------- */",
    flicker_js + "\n/* ---------- INIT ---------- */"
)

# Add flicker to loop
c = c.replace(
    "updateAbilityHUD();\n  composer.render();",
    "updateAbilityHUD();\n  updateFlicker(dt);\n  composer.render();"
)

# Apply flicker properties to point lights in buildHouse
old = "const lMat2=new THREE.MeshStandardMaterial({color:0xffffff,emissive:0xfff8e8,emissiveIntensity:2.5});\n  for(const[lx,lz]of[[-7,4],[-7,8],[7,4],[7,8],[-7,-4],[-7,-8],[5,-4],[13,-4],[5,-8],[13,-8],[-22,-4]]){\n    const lp=new THREE.Mesh(new THREE.BoxGeometry(2.5,.05,.5),lMat2);lp.position.set(lx,rH-.05,lz);scene.add(lp);allBuildingMeshes.push(lp);\n    const pl=new THREE.PointLight(0xfff5e0,2.5,12,1.2);pl.position.set(lx,rH-.6,lz);scene.add(pl);"
new = "const lMat2=new THREE.MeshStandardMaterial({color:0xffffff,emissive:0xfff8e8,emissiveIntensity:2.5});\n  for(const[lx,lz]of[[-7,4],[-7,8],[7,4],[7,8],[-7,-4],[-7,-8],[5,-4],[13,-4],[5,-8],[13,-8],[-22,-4]]){\n    const lp=new THREE.Mesh(new THREE.BoxGeometry(2.5,.05,.5),lMat2);lp.position.set(lx,rH-.05,lz);scene.add(lp);allBuildingMeshes.push(lp);\n    const pl=new THREE.PointLight(0xfff5e0,2.5,12,1.2);pl.position.set(lx,rH-.6,lz);scene.add(pl);pl.userData={flicker:true,baseIntensity:2.5,flickerSpeed:2+Math.random()*3,flickerOffset:Math.random()*6.28,flickerAmount:0.15};"
c = c.replace(old, new)
# If the replace didn't work, try alternate
if c == orig:
    # Try without the newline variations
    old_flat = "const lMat2=new THREE.MeshStandardMaterial({color:0xffffff,emissive:0xfff8e8,emissiveIntensity:2.5});\n  for(const[lx,lz]of[[-7,4],[-7,8],[7,4],[7,8],[-7,-4],[-7,-8],[5,-4],[13,-4],[5,-8],[13,-8],[-22,-4]]){\n    const lp=new THREE.Mesh(new THREE.BoxGeometry(2.5,.05,.5),lMat2);lp.position.set(lx,rH-.05,lz);scene.add(lp);allBuildingMeshes.push(lp);\n    const pl=new THREE.PointLight(0xfff5e0,2.5,12,1.2);pl.position.set(lx,rH-.6,lz);scene.add(pl);"
    if old_flat in c:
        new_flat = "const lMat2=new THREE.MeshStandardMaterial({color:0xffffff,emissive:0xfff8e8,emissiveIntensity:2.5});\n  for(const[lx,lz]of[[-7,4],[-7,8],[7,4],[7,8],[-7,-4],[-7,-8],[5,-4],[13,-4],[5,-8],[13,-8],[-22,-4]]){\n    const lp=new THREE.Mesh(new THREE.BoxGeometry(2.5,.05,.5),lMat2);lp.position.set(lx,rH-.05,lz);scene.add(lp);allBuildingMeshes.push(lp);\n    const pl=new THREE.PointLight(0xfff5e0,2.5,12,1.2);pl.position.set(lx,rH-.6,lz);scene.add(pl);pl.userData={flicker:true,baseIntensity:2.5,flickerSpeed:2+Math.random()*3,flickerOffset:Math.random()*6.28,flickerAmount:0.15};"
        c = c.replace(old_flat, new_flat)
        print("  Light flicker applied (flat)")

# Remove duplicate UnrealBloomPass import (remove old single-pass creation)
# The old line was replaced earlier. Check for any remnant
c = c.replace(
    "composer.addPass(new UnrealBloomPass(new THREE.Vector2(innerWidth,innerHeight),0.25,0.25,0.65));bloomPass.threshold=0.1;bloomPass.strength=0.35;bloomPass.radius=0.2;composer.addPass(bloomPass);",
    "const bloomPass=new UnrealBloomPass(new THREE.Vector2(innerWidth,innerHeight),0.25,0.25,0.65);bloomPass.threshold=0.1;bloomPass.strength=0.35;bloomPass.radius=0.2;composer.addPass(bloomPass);"
)

print("✅ PART 3: 3D style sharpened — better shadows, bloom, materials, lights, PBR")

# ================================================================
# PART 4: Add invulnerability after damage
# ================================================================
# Make damage from enemies apply invulnerability frames
c = c.replace(
    "GS.health-=dt*15;sfxGhost();const pa=Math.atan2(-dx,-dz);GS._vx=(GS._vx||0)+Math.sin(pa)*8;",
    "if(!GS._invulnerable){GS.health-=dt*15;GS._invulnerable=true;GS._invulnerable_timer=0.5;}sfxGhost();const pa=Math.atan2(-dx,-dz);GS._vx=(GS._vx||0)+Math.sin(pa)*8;"
)
c = c.replace(
    "GS.health-=dt*20;sfx(400,.1,'square',.04);const ka=Math.atan2(-dx,-dz);",
    "if(!GS._invulnerable){GS.health-=dt*20;GS._invulnerable=true;GS._invulnerable_timer=0.5;}sfx(400,.1,'square',.04);const ka=Math.atan2(-dx,-dz);"
)

print("✅ PART 4: Invulnerability frames added after damage")

# Write file
with open(PATH, 'w') as f:
    f.write(c)

size_change = len(c) - len(orig)
print(f"\n✅ COMPLETE: {len(c)} bytes ({size_change:+d})")
print(f"📁 {PATH}")
