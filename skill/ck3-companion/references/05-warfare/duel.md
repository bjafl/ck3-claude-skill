---
title: Duel
category: warfare
tags: [duel, combat, prowess, challenge, trial by combat, single combat]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Duel]
---

A duel is combat between two characters outside battle. Can end when one gets wounded or dies. Characters cannot duel if: child, Blind, Incapable, Pregnant, have disease trait, or both over 70 with Prowess below 10. Characters wear armor during duels (Tribal rulers fight shirtless).

## Issuing a Challenge

Duels start via events or character challenges (limited once per 5 years). If recipient refuses, challenger gains 150 Prestige while recipient loses 150. Challenge acceptance depends on Prowess difference, recipient opinion, and personality. AI rulers never challenge those 15+ Prowess higher unless Rationality very low. Two rulers at war cannot duel.

Duel types by requirement:

| Type | Challenger Requirements | Opponent Requirements | Effects |
|------|------------------------|----------------------|---------|
| Artifact Challenge | Claim on opponent's artifact | Has claimed artifact | Winner takes artifact; loser loses artifact claim |
| Sparring | Chivalry or Futuwaa tradition | Knight | Victor: 75% gain random positive modifier (10 yrs), 25% gain negative (10 yrs) |
| Single Combat | Stalwart Leader perk, Martial Admiration/Druzhina/Fragile Peace tradition, or Nomadic/Sōryō/Expansion political movement | Rival or Nemesis | Victor loses Stress; loser gains Stress |
| Anger Release | Irritable trait + 1+ Stress | - | Challenger gains +5 Dread; victor loses Stress, loser gains Stress |
| Punishment | Wrathful trait | Criminal (not liege) | Winner: loser executed (if crime allows) or imprisoned; loser wins: challenger gains 100 Stress |
| Rite of Passage | Rite of Passage decision | Adult | Winner gains +10 vassal/culture Opinion, -10% Stress gain (10 yrs); loser gains +25% Stress gain (10 yrs) |
| Prowess Coup | Attempt to Overthrow Liege decision | Liege | Winner replaces liege; loser dies (personal champions allowed) |
| House Head Challenge | House Unity is Impassive/Competitive/Antagonistic | House Head | Winner becomes house head; loser gains Weak Hook |
| Trial-by-Combat | Performative Honor tradition | Criminal (not liege/vassal) | Winner chooses reward: Gold, Stress, Weak Hook, or Death (personal champions allowed) |

Accolades on winning side gain +10 to +250 Glory (based on Prowess advantage). Defeating Rival grants +25 Glory.

## Mechanics

Two tracked values:
- **Likelihood of Success**: Overall performance (offensively/defensively); sufficient lead ends round with skill victory
- **Risk of Injury**: Overextension measure; if close to Likelihood of Success, possibility of loss by mistake (chance = excess Risk over Likelihood). If both lose by mistake, attacker wins.

Duels last 2-4 rounds; from round 3 onward, victory increasingly likely. If no victor after round 4, higher Prowess wins by Sudden Death (tied Prowess = coin flip).

Each round, both choose one of three combat moves weighted by Prowess (higher Prowess = better moves more likely). Moves affect tracked values differently; some have additional effects. Either character can gain/lose Duel Edge (modifies Prowess during duel).

### AI Move Selection

- High Boldness/Vengefulness: best Likelihood of Success
- Low Boldness/Vengefulness: least Risk of Injury
- High Rationality: middle ground
- No high/low traits: random

### Regular Combat Moves

| Move | Likelihood | Risk | Prowess | Other |
|------|-----------|------|---------|-------|
| Wait & Hope | Low | Medium | 0-15 | - |
| Unsure Attack | Medium | High | 0-15 | - |
| Enthusiastic Onslaught | High | Very High | 0-15 | - |
| Clouded Vision | None | Low | 0-15 | Opponent -4 Duel Edge |
| Headbutt | Medium | High | 0-15 | Both -4 Duel Edge |
| Guard | Low | Low | 6-20 | - |
| Probing Attack | Medium | Medium | 6-20 | - |
| Onslaught | High | High | 6-20 | - |
| Put the Boot In | Very High | Very High | 6-20 | - |
| Surprise Attack | Random | Medium | 6-20 | - |
| Taunt | None | Medium | 6-20 | Opponent gains Stress modifier |
| Strict Guard | Low | None | 8+ | - |
| Confident Attack | Medium | Low | 8+ | - |
| Expert Onslaught | High | Medium | 8+ | - |
| Lightning Assault | Very High | High | 8+ | - |
| Tire Opponent | Low | None | 8+ | Increases opponent Risk of Injury |
| Attempt Disarm | Low | Medium | 12+ | Opponent -6 Duel Edge |

### Special Combat Moves

Special moves more effective/bonus but have requirements; 30% chance appear if requirements met.

| Move | Likelihood | Risk | Requirements | Other |
|------|-----------|------|--------------|-------|
| Hail Mary | Very High | High | 10+ Prowess difference | - |
| Disheartening Speech | None | Medium | 18+ Diplomacy | +5 Prestige per Diplomacy point |
| In Command | None | Low | 18+ Martial | Opponent -2 Duel Edge (Arrogant); -4 (not Arrogant) |
| Like a Viper | High | Medium | 18+ Intrigue | Increases opponent Risk of Injury |
| Legendary Technique | High | Low | 18+ Learning | - |
| Silvered Vision | Medium | None | 18+ Stewardship, 20+ Gold, not Maimed | Costs 20 Gold |
| Mocking Boast | None | None | Higher Prestige, opponent not Humble | Opponent -2 Duel Edge; +40 Stress (Arrogant) or +20 (not) |
| Master of Terrain | High | Low | Terrain bonus trait | +2 Duel Edge |
| Berserkergang | Very High | Medium | Berserker trait | -20 Stress |
| Hard Grit | High | None | Shieldmaiden trait | +4 Duel Edge |
| Feint & Stab | High | Medium | Hunter trait | +4 Intrigue modifier (5 yrs) |
| Butchery | High | Medium | Raider trait | +2 Dread per 2 Prowess |
| Stoic Veteran | Medium | None | Varangian trait | +Health Boost modifier (5 yrs) |
| Blade Dance | High | Low | Blademaster trait | +5 Prestige per Prowess point |
| Divine Wrath | Low | None | Zealous trait | Piety by opponent faith: Righteous +10, Astray +25, Hostile +50, Evil +75 |
| Fueled by Pain | Medium | Medium | Deviant trait/secret | +2 Duel Edge (normal); +4 (Severely Wounded); +8 (Brutally Mangled) |
| Something to Hide | None | None | Hook on opponent; not death duel | +4 Duel Edge (Weak Hook); +8 (Strong Hook) |
| An Unexpected Ally | Very High | None | Duel in Africa/Persia/India/Burma; terrain Farmlands/Floodplains/Jungle/Oasis/Wetlands; death duel | Appears once only |

## Related Topics

See [Warfare Overview](warfare-overview.md), [Knights](knights.md), [Army](army.md).
