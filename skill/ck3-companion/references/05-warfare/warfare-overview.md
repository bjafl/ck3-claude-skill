---
title: Warfare Overview
category: warfare
tags: [war, battle, siege, holy war, raiding, war score, truce]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Warfare]
---

Warfare is the primary military mechanism for expanding a character's realm through force. All wars require a Casus Belli that defines outcomes for victory, defeat, or white peace. Characters cannot declare war while in debt or while armies are raised (unless they have Nomadic government), and vassals who declare independence leave any ongoing wars started by their liege.

## Battles

### Combat Phases

Battles begin when two hostile armies occupy the same barony. A terrain's Combat Width determines how many troops can engage simultaneously. Each battle progresses through four phases:

- **Maneuver Phase (2 days)**: Armies prepare and commanders roll for initial Advantage.
- **Early Battle Phase (12 days)**: Armies inflict daily damage but cannot retreat. Defeated armies have routed casualties become fatal casualties, fully destroying the army.
- **Late Battle Phase**: Fighting continues with daily damage until one side's soldiers run out of Toughness or retreat. Retreating converts all remaining soldiers to routed casualties.
- **Aftermath Phase (3 days)**: Winners chase routed armies to convert remaining casualties to fatal ones. Defeated armies move to adjacent baronies and cannot be commanded until traveling several baronies away.

### Advantage Modifier

Advantage is a battle-long modifier that increases damage for all troops on a side. Sources include traits, terrain, buildings, and the commander's Martial skill. Commanders roll d10 every 3 days to increase their Advantage, influenced by various modifiers and traits.

Starting Advantage modifiers:
- +30 defending across strait
- +20 defending across large river
- +10 defending across river
- +10 from Pagan combat advantage
- +5 if liege leads army
- +5 from Never Back Down martial lifestyle perk
- +5 from Chivalry focus
- -10 if realm in debt
- -10 if army is gathering
- -10 if army low on supplies
- -25 if army out of supplies
- -30 if attacking across sea

### Capturing Commanders

Defeated commanders may be captured (10% base chance) using two escape/capture scores. Capture chance is affected by:

| Factor | Effect |
|--------|--------|
| Stalwart Leader Perk (player) | +100 escape score |
| Stalwart Leader Perk (AI) | +30 escape score |
| Prowess | Capture score × (30 - prowess) ÷ 30, minimum 0.1 |
| Craven trait | Capture score ÷ 2 |
| Army stackwiped | Escape score ÷ 5 |
| Brave trait | Capture score × 2 |
| One-Legged or Maimed trait | Capture score × 3 |

### Siege

Sieges occur automatically when non-raiding armies stop in baronies with Fort Level, provided troop count exceeds the garrison. Moving a besieging army ends the siege and resets all progress unless another army in that barony still exceeds garrison strength.

When a siege completes, the barony is occupied: it displays owner/occupier stripes on the map, produces no taxes/levies/control/development, and neither side can construct buildings. Garrison resets to 25 but replenishes based on Garrison Reinforcement Rate. County control decreases by 40 (80 with Pillage legacy, negated with Enduring Hardships perk).

Unfortified baronies cannot be sieged but auto-occupy if all fortified baronies in the county are occupied. War Score shifts toward the occupier based on realm size, with bonuses for fulfilling objectives.

Besiegers suffer 1% attrition per month. Combat while besieging a fortified holding makes besiegers the attackers, reversing terrain advantages and applying additional penalties.

#### Siege Progress

Siege Progress (0-100+ depending on Fort Level) accrues daily until the barony is occupied. Required progress = 100+75 per Fort Level, reduced by the garrison percentage (e.g., half garrison = half progress required).

Daily Siege Progress = 1 + 0.05 for each 200 besieging soldiers exceeding garrison. Siege weapon men-at-arms add additional progress. Traits and modifiers can enhance contributions, but Daily Siege Progress never drops below 0.5 per day.

Siege weapon effectiveness by fort level:

| Fort Level | None | 1 Tier | 2 Tiers | 3 Tiers | 4+ Tiers |
|------------|------|--------|---------|---------|----------|
| 1-3 | 100% | 100% | 100% | 100% | 100% |
| 4-5 | 70% | 100% | 100% | 100% | 100% |
| 6-10 | 50% | 70% | 100% | 100% | 100% |
| 11-15 | 35% | 50% | 70% | 100% | 100% |
| 16-30 | 25% | 35% | 50% | 70% | 100% |
| 31+ | 17% | 25% | 35% | 50% | 70% |

#### Siege Statistics

Defending forts track three statistics (Supplies, Sickness, Walls), each with three incremental stages:

| Statistic | Stage 1 | Stage 2 | Stage 3 |
|-----------|---------|---------|---------|
| Walls | None | -5% Morale (one-time) | -15% Morale (one-time) |
| Sickness | None | +10% Daily Siege Progress | +20% Daily Siege Progress |
| Supplies | None | -10% time between events; 2.5% daily assault casualties | -30% time between events; 1% daily assault casualties |

Siege Events occur every 20 days (14 with Military Engineer trait, reduced by 10-30% with wall breaches):

| Event | Weight | Effect |
|-------|--------|--------|
| Stalemate | 20 | None |
| Desertion | 20 | +5.0 Siege Progress |
| Starvation | 15 | Changes Supplies by one stage |
| Disease Outbreak | 15 | Changes Sickness by one stage |
| Breach | (30 × siege weapon tier) - (fort level × 2) | Changes Walls by one stage |

After walls are breached, assault adds large daily Siege Progress at casualty cost (0.2 Daily Siege Progress per 100 soldiers).

**Inferred:** Siege weapon men-at-arms are essential for effective sieges. Adding soldiers without siege equipment provides negligible progress and leaves armies unable to assault, forcing prolonged damaging sieges. Tribal characters often lack siege weapons and should prioritize the Onager innovation. The Sappers perk (+0.1 Daily Siege Progress) and Engineered Destruction perk (+40% siege men-at-arms progress) significantly reduce siege duration. Siege tiers have diminishing returns; spreading men-at-arms across multiple sieges is often better than concentrating them.

### Prestige and Fame Gain

Battle victories grant prestige, fame, piety, or devotion. War leaders gain fame against enemy leaders or allies; otherwise combatants gain prestige and devotion (including allies fighting or fighting vassals).

## War Score

War Score ranges -100 to +100, measuring which side is winning. Points gained by one side are subtracted from the other. Score is earned through battles, occupying holdings, capturing important prisoners, and especially controlling the Casus Belli's war target (the objective territory).

If either side controls all de jure counties of the disputed title, they gain 1% war score monthly. Losing even one county resets control score to 0 but returns if that county is recaptured. Neither side gains from control if both hold part of the disputed land. (Example: War for Duchy of Lancaster with 4 counties means attacker gains 1%/month only if holding all 4.)

This doesn't apply to wars claiming the realm's highest title (e.g., Kingdom of England claims accumulate control score even if attacker holds just one county, unless an Empire exists and claims the kingdom's liege).

Bonus War Score sources:
- +100 for capturing enemy ruler
- +50 primary heir, +25 secondary heir, +10 tertiary heir
- +10 for occupying enemy capital

Battle-earned war score depends on losing army size relative to total strength. Holding bonuses scale with defender's total holdings inside and outside the war target. Against rulers, battles grant up to 50% war score; against adventurers there is no limit.

### Ending Wars

- **White Peace** (at +30 War Score): Winning side calls for this.
- **Enforce Demands** (at +100 War Score): Winning side enforces full war objectives.
- **Surrender**: Players can always surrender, or losers must surrender at -100 War Score (modified by Peace Acceptance and Peacemaker Perk). AI eventually surrenders at +100 to prevent further captives/damage.
- **War Condition Invalidated**: Wars end if Casus Belli requirements no longer apply (e.g., defending county lost).

### War Contribution

In wars with allies, each side tracks War Contribution percentages. Upon war end, gold, prestige, or piety is distributed among allies based on contribution.

If a war lasts 2+ years and an ally has 0% contribution, they lose -20 opinion with the war leader and must pay gold/prestige or promise contribution within a year (breaking it costs a Fame level and -50 opinion).

## Holy Wars

Holy Wars use Holy War Casus Belli. Unlike regular wars, rulers of the defending faith can join without alliances. Defenders can convert to attacker's faith (100 Piety, 3 Devotion) to achieve white peace.

### Great Holy Wars

Great Holy Wars (only by Heads of Faith with Warmonger/Armed Pilgrimages/Struggle and Submission tenets or Special Doctrines, not imprisoned) target kingdoms ruled by different faiths. If victorious, all kingdom titles are seized and distributed by War Contribution. Faith must have 75% fervor.

Attacking faith members can designate Beneficiaries (unlanded, non-heir dynasty members) to receive proportional titles. No white peace option; capturing the enemy leader/heir grants no war score. Victory decreases attacker fervor by -30 (+25 defender), or defeat costs -25 attacker fervor.

Victorious contributors and knights gain Crusader (Christian), Mujahid (Muslim), or faith-specific Warrior of the Faith traits. Excommunicated trait is removed.

AI rulers are less afraid of outnumbering armies during Great Holy Wars.

#### Directed Great Holy Wars

Temporal Heads of Faith declare these. Victorious kingdom goes to the Head of Faith. Same-faith rulers can join and gain piety/titles based on contribution.

#### Undirected Great Holy Wars

Spiritual Heads of Faith declare these. During preparation, rulers of both faiths can donate gold (receive piety equal to half) or pledge military support.

War Chest distribution: 20% divided among attackers pledging support at preparation end; remainder divided if faith wins.

Pledging support requires military strength and ends all inter-pledger wars. Attackers gain piety; War Chest gains prestige and piety by pledger rank:

| Rank | Piety | War Chest Prestige | War Chest Piety |
|------|-------|-------------------|-----------------|
| Baron | 30 | 250 | 75 |
| Count | 60 | 500 | 150 |
| Duke | 90 | 1000 | 300 |
| King | 120 | 1500 | 600 |
| Emperor | 150 | 3000 | 1200 |

Withdrawing pledges costs one Devotion. Pledgers can spend Piety to change target kingdom (101+ days before war start).

If pledge caller dies during preparation, the war still starts.

War begins if attacker strength exceeds 33% of defender. Attackers with highest contribution gain the kingdom.

#### Great Holy War Unlock Requirements

Faiths unlock Great Holy Wars after 1100 (or earlier with conditions) by having:
- Correct doctrines
- Head of Faith existing and not imprisoned
- 35+ counties following the faith
- Fervor above 65%
- 10+ years since another faith unlocked

Faith-specific unlock conditions:
- Catholic: 1095 with Jerusalem not Christian; 1000 with Byzantine emperor or Ankyra/Athens/Constantinople/Corinth not Christian; 800 with Cologne/Halberstadt/Paris/Venaissin/Toulouse not Christian; anytime with Rome not Christian
- Islam: After Christianity unlocks, if any holy site or Jerusalem/Mecca not Muslim
- Any faith: After both Christian/Muslim unlock, if any holy site in Hostile/Evil faith realm; 800 year with any two holy sites in different-faith realms

#### Great Holy War Targeting Weights

AI targets: 100× key religious holdings (Jerusalem for Catholics/Jews, Mecca/Medina for Muslims), 75× kingdom where Head of Faith was human-sacrificed, 50× kingdoms with holy sites, 40× heartland kingdoms, 30× frontier, 20× fringe, 10× stretch, 1× others. Distance from Head of Faith (if landed) or primary religious site divides these. Same-faith kingdom-holders receive 20× multiplier if not controlling entire kingdom.

## Raiding

Raiding attacks holdings without war, gaining loot. To raise raider armies, characters need:
- Unreformed faith
- Tribal/Wanua government
- Practiced Pirates tradition
- Ghazi Status tax decree
- Legacy of Piracy dynasty modifier
- [Roads to Power] Frontier administration
- [Khans of the Steppe] Nomadic government
- Meritocratic Khanate government

Raiders carry loot based on army size. Embarkation requires Longships/West African Canoes innovation or Practiced Pirates tradition. Selected raider armies show holding loot amounts. Raiding armies cannot move, letting defenders raise forces. If defeated before returning home, all loot is recovered. Raider maintenance is 50% reduced.

Raid Intents determine loot conversion:

| Intent | Loot Conversions (Gov dependent) | Raid Speed | Effects | Requirements |
|--------|-----------------------------------|-----------|---------|---------------|
| Pillage | 100% Gold | 100% | -1.5 Prestige per Loot (non-Tribal/Wanua/Nomadic) | - |
| Adventure | 100% Gold + Prestige | 80% | No hostile attrition; +300% loot capacity | Longships |
| Capture | 50-25% Gold (dependent) | 70% | +15% character imprisonment | - |
| Terrorize | 100% Prestige + 10% Dread | 40% | +30% sack offer; 25% county loses 5 Fort + 75% Garrison (5 years); 25% loses 1 Development; 25% holding loses 1 building | Scorched Earth/No Quarter legacy |
| Plunder | 100% Gold + 150% Herd | 40% | 2% innovation gain | Culture head |

Raided holdings cannot be raided again for 5 years (-50% taxes, +50% building time, -10% development growth). Raids on capital holdings may capture/kill courtiers/family. Raider commanders gaining 20+ raids have increasing trait chance equal to raid count.

Rulers with raided holdings may sack the county (30% if commander, 50% with Raider trait), choosing treasure (more gold/prestige, -40 development) or slaves (if capital under 15 development: +40 capital development, -1 sacked development, -80 sacked progress). Either grants "Recently Sacked" modifier (20 years, prevents future sacks, +20 popular opinion) and +10 stress if Compassionate/Forgiving.

Raided rulers gain decaying -15 opinion (+1.47/year) toward raiders.

With Northern Lords DLC (requires peace, commander leading, castle target, Longships/Adventure legacy 2): 20% (or 40% for North Germanic/Adventure legacy 2) trade offers (10 Loot, +20 opinion, 5-year raid block, +20 popular opinion to previously raided county).

Raider armies can fight barterer armies for barter goods.

## Capturing Characters in Holdings

Characters in just-occupied or -raided holdings have 35% base capture chance (reduced by Intrigue: -1% per point, max -20%; reduced by Prowess: -0.5% per point, max -15%; +20% from Pillage legacy 3).

Non-desirable captured characters are killed instead (e.g., by peasant armies). Desirable targets include: landed characters, those with parents/landed spouses/landed close family, those with high skill ratings (diplomacy/martial/stewardship/intrigue/learning), physician or mystic lifestyle traits.

Excluded from capture: defenders with unretreated armies or imprisoned characters.

## Initial Wars

The game starts with these wars:

| Attacker | Defender | Casus Belli |
|----------|----------|------------|
| Aghlabid | Byzantine Empire | Conquer Duchy |
| Hadithan-Ana | Abbasid Empire | Invade Kingdom |
| Asturias | al-Andalus | Claim |
| Saffarid | Tahirid | Invade Kingdom |
| Tulaytulah Burtughal | al-Andalus | Independence |
| Italy | Apulia | Conquer Duchy |
| Jórvík Uppland | Northumbria, Mercia, Wessex | Varangian Adventure |
| The Suðreyjar | East Anglia, Mercia, Wessex | Varangian Adventure |
| The Suðreyjar | Northumbria | Varangian Adventure |
| Seljuk Empire | Byzantine Empire | Claim |
| Norway | England | Invade Kingdom |
| Normandy | England | Invade Kingdom |
| Ruhunu | Chola Kingdom | Claim |
| Jamtaland | Norway | Claim |

Mogyër Confederation also starts at war with Bulgaria using Migrate to Pannonia CB if Hungarian Migration rule is set to Immediate.

## Truce

Wars end with 5-year truces. Declaring war during active truce costs attacker -250 prestige, -1 fame level, and -50 general opinion (3 years). Decisions ignore this penalty.

Diplomacy perks:
- Defensive Negotiations: enables Purchase Truce interaction
- Flexible Truces: -25% Truce Time; no prestige penalty for breaking truces

## Related Topics

See [Casus Belli](casus-belli.md), [Army](army.md), [Hired Forces](hired-forces.md), [Knights](knights.md), [Duel](duel.md).
