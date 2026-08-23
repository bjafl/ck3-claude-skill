---
title: Army
category: warfare
tags: [army, levies, men-at-arms, knights, soldiers, commanders, supply, attrition]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Army]
---

Armies are controlled groups of soldiers that attack enemy armies or siege holdings during wars. Hovering over allied armies displays their current orders. Armies can be automated via the Military tab for AI control. After armies complete half a movement between baronies, they become movement-locked until reaching their destination. Armies crossing sea zones embark onto fleets, costing Gold proportional to size, raising maintenance +25%, and consuming supplies after 30 days at sea.

## Unit Stats

Five stats apply to all units:

- **Damage**: Each point causes 0.03 damage during the battle phase.
- **Toughness**: Reduces losses from damage. Each point allows absorbing 1 damage before losing all strength.
- **Pursuit**: Each point causes 0.17 damage during the retreat phase.
- **Screen**: Each point blocks 0.33 damage during the retreat phase.
- **Strength**: Represents soldier count and affects total stats. Heavy cavalry/Asawira: 50 soldiers; Elephant cavalry: 25; Siege weapons: 10; other men-at-arms: 100; Levies: their total count.

### Damage Dealing

Total army Damage gets modified by +5% per Advantage point (for the advantaged side). This is then modified by terrain width: ((Enemy + Ally) Strength × (0.5 × Terrain width)). Example: 1000 Levies vs. 500 Levies on Plains = 750 Levy damage output; on mountains (0.5× modifier) = 625 Levy equivalent. Damage distributes to enemy army based on strength composition (e.g., 80% to 8000 Levies, 15% to 1500 Archers, 5% to 500 Spearmen).

Levies typically take most casualties as they compose the bulk with low Toughness. Damage gradually shifts toward men-at-arms then knights (highest Toughness, lowest Strength). Army quality 'upgrades' during battle as low-ranking soldiers are defeated.

## Rallying and Disbanding Armies

Armies rally at "Rally Points" (default at capital; up to 10 total per realm). Cannot raise armies where enemy armies exist. Cannot disband armies when enemies are nearby (within ~1 county or adjacent sea zone).

Armies consist of:
- Individual Knights
- MAA regiments
- Levies from holdings you control
- Levies from vassal contributors

Divide and regroup manually via "Split Off New Army" or "Split in Half." Special option: "Split off Hired or Special Soldiers" for mercenaries/special units.

Raider armies cannot divide outside your realm.

Rally time depends on realm size/width (small realms take days; continental empires may take months). MAA/Knights arrive based on distance to capital; Levies depend on origin holdings. Use "Raise Local Armies" if full rally takes too long. 

Armies can only disband in friendly territory during wars. Disbanding far from capital/origin incurs time penalties (months) before next rally.

## Reinforcing Armies

Armies must be in friendly territory or disbanded to reinforce (monthly, though complex bugs can prevent it).

Men-At-Arms reinforce at 10% of maximum capacity per day with tripled cost per regiment.

Levies reinforce based on Levy Reinforcement Rate (base similar to Garrison Reinforcement Rate, modified by Martial skill, Marshal's "Organize Levies," building upgrades). Reinforce individually by origin holding.

## Quality

Army quality (based on unit composition) shows skill level and determines appearance (peasant clothing for all-levy armies, high-quality armor for knight-only armies). This matters because outnumbered skilled armies deal significantly more damage than similar-quality enemies. Example: Takes 3.3× as many Levies to defeat one Armored Footman regiment in Plains combat.

## Commander

Each army has one Commander (character using Martial skill to increase Advantage). Commander traits affect battles and bonuses outside battle. Commanders can be any Vassal (unless in civil war) or Courtier allowed by Martial Custom. Commanders can be injured, maimed, or killed in battle (chance depends on Prowess; higher Prowess decreases chance; reduced if army outnumbers enemy or difficulty lowered). Each month, low-Health commanders without current-terrain trait have small death chance. Defeated army commanders have 10% capture/imprisonment chance.

## Knights

_See [Knights](knights.md)_

Knights are elite Characters assigned to combat, different from other fighters.

## Basic Soldiers

### Levies

Conscripted peasants making up army bulk; cheap/free to maintain and reinforce. Available to all governments except Nomadic and Adventurer. Numbers determined by ruler's domain holdings and vassal/Realm Priest contributions. Base: 10 Damage, 10 Toughness, 3 Gold/month per 1000 when raised. Stats remain fairly static across Eras.

### Horde Riders

Nomadic government only. Base 15% of ruler's Herd converts to Horde Riders (consuming equivalent Herd). Convertible to men-at-arms regiments. Switch to special soldiers if government changes. Base: 12 Damage, 12 Toughness, 10 Pursuit, 15 Screen, no maintenance when raised.

## Men-at-Arms

Trained regiments excelling in specific roles, each with unique stats. Counters apply: each MAA type counters ≥1 other, reducing countered Damage by -45% (1:1) to -90% (2:1) or worse. Circle of counters generally runs: Skirmishers > Heavy Infantry > Spearmen > Cavalry > Archers > Skirmishers. Unique types (Archer Cavalry, Camel Cavalry, Elephant Cavalry) explicitly countered per type.

Most MAA have favorable/unfavorable terrain (non-percentage constants). Reinforce at 10% maximum per month; reinforcement cancellable via "Monthly Reinforcement" toggle.

Rulers have limited MAA regiments/sizes; existing ones upgrade for same recruitment cost. Can downsize (lower cost) or destroy (unrefunded). Regiments inherited by primary heir unless heir already has maximum regiments.

Base limit: 2 (Count) regiments, max size 3. Notable modifiers: Era Innovations increase regiments +1 each, size +2/3/4/5 per Era; ascending to Duke/King/Emperor grant +1/+2/+3 more regiments. Cannot recruit above limit; exceeding existing limit increases maintenance +20% per excess regiment.

Payment varies by government: Gold (most); Tribal (2× Gold for creation, -30% maintenance); Wanua (Barter Goods, -30% maintenance); Nomadic (Herd equal to regiment size if upgradable from Horde, else full Gold). Most MAA triple maintenance when raised, costing same to reinforce. Elephants and House Guards don't triple. MAA increase Camp Provisions cost for adventurers.

Regiments can station in domain holdings, gaining stat bonuses from buildings.

Default size: 100. Heavy Cavalry (except Black Armored): 50; Ballistrai, Ayrudzi, Asawira, Kheshig, Heavy Horse Archers: 50; War Elephants: 25; Siege weapons: 10.

### Regular Men-at-Arms

Available to all cultures (prerequisites met):

| Regiment | Cost | Raised | Provisions | Damage | Tough | Pursuit | Screen |
|----------|------|--------|------------|--------|-------|---------|--------|
| Light Footmen | 45 | 0.45 | 3 | 10 | 16 | 10 | 16 |
| Bowmen | 55 | 0.6 | 7 | 25 | 10 | 0 | 0 |
| Pikemen | 75 | 0.9 | 12 | 22 | 24 | 0 | 0 |
| Light Horsemen | 85 | 1.05 | 7 | 22 | 15 | 30 | 30 |
| Armored Footmen | 90 | 1.2 | 7 | 32 | 22 | 0 | 0 |
| Armored Horsemen | 200 | 2.1 | 21 | 100 | 35 | 20 | 0 |
| Crossbowmen | 88 | 0.9 | 7 | 42 | 18 | 0 | 0 |
| Handgunners | 76 | 1.05 | 7 | 52 | 12 | 0 | 5 |
| Horse Archers | 135 | 1.35 | 7 | 36 | 18 | 40 | 30 |
| Varangian Guards | 72 | 0.96 | 7 | 45 | 32 | 10 | 5 |
| Handpicked Faithful | 67 | 0.9 | 3 | 38 | 28 | 5 | 5 |
| Fire Lancers | 88 | 0.9 | 7 | 40 | 8 | 0 | 0 |
| Jomsviking Pirates | 63 | 0.63 | 3 | 30 | 30 | 40 | 40 |
| Order Knights | 90 | 1.2 | 12 | 36 | 26 | 0 | 0 |

### Title Men-at-Arms

Tied to specific titles (Domicile governments: Administrative, Celestial, Meritocratic). Move with title on ownership change; may be lost on succession. Typically smaller starting size.

### Traditional Men-at-Arms

Available through traditions and eras. Adventurers with Take the Custom Where It Comes can recruit them per county culture. _Not covered on the wiki_ (too many to list individually; see in-game or wiki tables for detailed stats).

### Regional Men-at-Arms

Available through regional innovations (Caballeros, Camel Riders, Hobelars, Paiks, Sahel Horsemen, Tiefutu, War Elephants, Ballista Elephants, etc.). _Not covered on the wiki_ (detailed table requires game reference).

### Cultural Men-at-Arms

Require culture-specific innovations (Chasseurs, Landsknechts, Palatini, Vaulter Infantry, Rocket Carts, Teulu). _Not covered on the wiki_ (detailed stats game-dependent).

### Dynastic Men-at-Arms

Available only to dynasties with specific legacies:

| Regiment | Cost | Raised | Requirements |
|----------|------|--------|--------------|
| House Guard | 50 | 1 | Warfare legacy completed; max 1 |
| Asawira | 300 | 3 | Brilliance legacy 4 |
| Kheshig | 225 | 2.25 | Nomadic legacy 4; max 1 |

### Siege Weapons

Cannot fight in battle but increase Siege Progress. Western (Onagers, Mangonels, Trebuchets, Bombards, Torch-Bearers) and Chinese/Korean/Japonic versions have identical stats:

| Weapon | Daily Siege | Max Fort | Cost | Provisions | Requirements |
|--------|-------------|----------|------|------------|--------------|
| Onagers/Siege Crossbows | +0.2 | 5 | 60 | 6 | Onager innovation |
| Mangonels/Cloud Ladders | +0.3 | 10 | 66 | 12 | Mangonels innovation |
| Trebuchets/Siege Towers | +0.4 | 15 | 78 | 18 | Trebuchet innovation |
| Bombards/Fire Dragons | +0.6 | 30 | 96 | 24 | Gunpowder innovation |
| Torch-Bearers | +0.1 | 5 | 30 | - | Nomadic government |

### Retinue Men-at-Arms

Available to rulers with Accolade rank 3-6. Twice as effective at countering MAA; stats scale with culture era. Examples: Retinue Archers, Retinue Camel Riders, Retinue Crossbowmen, Retinue Handgunners, Retinue Horse Archers, Retinue Lancers, Retinue Outriders, Retinue Pikemen, Retinue Skirmishers, Retinue Vanguard, Retinue War Elephants. _Not covered on the wiki_ (full stat tables game-era-specific).

### Outcasts Men-at-Arms

Adventurers using Levy the Outcasts decision or completing criminal contracts gain: Bandits, Looters, Marauders, Poachers. Lost upon succession.

### Nomadic Men-at-Arms

Available to Nomadic government rulers. Way of the Nomad trait holders can recruit even with different government.

| Regiment | Cost | Raised | Provisions | Damage | Tough | Pursuit | Screen |
|----------|------|--------|------------|--------|-------|---------|--------|
| Steppe Raiders | 76 | 0.94 | 7 | 22 | 15 | 30 | 30 |
| Heavy Horse Archers | 157 | 1.57 | 21 | 92 | 42 | 24 | 24 |
| Nomad Lancers | 190 | 2 | 21 | 120 | 30 | 20 | 0 |

## Supply

Armies carry supplies; all can carry ≥100 units (Living Off the Land perk raises to 300). Start with 100 Supply when raised. Consume monthly in baronies with lower Supply Limit than army size; gain in owned/occupied/allied territory up to barony limit. Low Supply applies Advantage penalties; complete depletion causes larger penalty plus monthly Attrition damage.

### Supply Limit

Base barony limit: 2000; minimum: 1000. Coastal baronies: +25%. Affected by buildings, terrain, county development. Temporary/permanent modifiers (Smuggling Rings, Saharan Province, Al-Yamnat, Grand Canal) also affect.

## Attrition

Army losses from various factors:

- Besieging/Raiding armies: 1% attrition per month
- Out of Supply armies: 5% attrition per month
- Moving from one hostile county to another hostile county (not adjacent to ally): instant 5% loss (minimum 100). Raiding armies by rivers and nomads in steppe exempt. Reaver trait reduces by 75% (minimum 25).

## Special Soldiers

Maintenance-free armies from decisions/historical rulers; don't reinforce. _Not covered on the wiki_ (detailed list requires historical lookups; game tracks by ruler/year).

## Related Topics

See [Warfare Overview](warfare-overview.md), [Hired Forces](hired-forces.md), [Knights](knights.md), [Casus Belli](casus-belli.md).
