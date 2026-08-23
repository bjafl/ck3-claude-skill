---
title: Situations
category: realm-and-succession
tags: [situations, disasters, dynastic cycle, silk road, seasons]
game_version: "1.19"
dlc: [Royal Court, Khans of the Steppe]
sources: [https://ck3.paradoxwikis.com/Situation]
---

Situations are major historical incidents involving multiple rulers unfolding over time. They progress through phases, with each phase affecting rulers differently. This document covers natural disasters, the Dynastic Cycle, the Silk Road, and steppe seasons.

## Natural Disasters

Natural disasters cannot occur in the first 10 years of gameplay. Afterward, one of each type occurs yearly. Selecting a disaster shows affected counties with a flashing red border. Disasters are 2x less likely in a duchy's de jure capital, 4x less likely if also a kingdom capital, and 10x less likely in regions that recently experienced disasters.

Natural disaster situations affect county owners and their lieges. Each disaster has three severity levels and three phases lasting specific durations.

**Phase 1: Warning (40 days)** — At day 20, rulers can gain 10 Stress and enter a regency for 10% cheaper recovery contributions (no Stress if already in regency).

**Phase 2: Impact (30 days)** — All affected rulers lose 50 Legitimacy (100 if Hegemon of China). Locations lose Control, no longer gain Development, and receive severity-based modifiers for 25 years. Every 7 days, characters die. Armies in the region have 25-75% chance to be damaged and lose supplies (by size). Rulers receive random negative events, and terrain visibly changes.

**Phase 3: Recovery (15 years)** — All affected rulers suffer −0.25 Monthly Legitimacy. Rulers can pay contributions for bonuses. Cost depends on affected county count, severity, tax income, and culture innovations. After all mandatory contributions are paid, the situation ends in 2 more months, removing all penalties. Multi-realm disasters require separate payments per realm.

### Recovery Contributions

| Contribution | Cost | Effects | Mandatory |
|---|---|---|---|
| Housing Reconstruction | Very low | +25 Legitimacy (independent), +150 Prestige/Piety (non-admin vassal), +30 Influence (admin), +60 Merit (celestial), +25% Development Growth 25y, +15% Holding Taxes 10-15y | Yes |
| Survivor Recovery | Moderate | +25 Legitimacy, +150 Prestige/Piety, +30 Influence/+60 Merit, +10% Control Growth 10y, +10 Popular Opinion 10y, −15-10% Holding Taxes | Yes |
| Debris Removal/Land Drainage | Moderate | +25 Legitimacy, +150 Prestige/Piety, +30 Influence/+60 Merit, Keeper of Order modifier, −75% Levy Reinforcement 10y, −10% Building Construction Cost 5y | Yes |
| Memorial Fortifications | High | +50 Legitimacy/+350 Prestige/Piety/+60 Influence/+100 Merit, Memorial Builder/Fortifications modifiers | No |
| Refugee Resettlement | High | +50 Legitimacy, resource bonuses, −25% Building Construction Cost, +25% Development Growth, +15 Popular Opinion, enhanced with Rightful Ownership/Manorialism (15-35y), reduced Domain Limit (5-10y) | No |
| Aid for Victims | Very high | +50 Legitimacy, +350 Prestige/Piety/+60 Influence/+100 Merit, Disaster Relief Savior modifier, +30 Opinion with Head of Faith, +0.5 Monthly Development/+25% Control Growth/+15 Popular Opinion/+3 Plague Resistance (25-35y) | No |
| Send Department Aide | High | Requires Department Aide position, +60 Merit, +150 Influence, Treasury/bonus by councilor, specific benefits per position | No |

Flooded counties gain Good Fertility modifier (10 years): +25% Supply Limit, +15% Development Growth, (Khans of the Steppe) +25% County Fertility Growth.

### Earthquake

Affects epicenter county and all adjacent counties. More likely in Asia Minor, China, Middle East, North-Eastern Africa, Indonesia, Japan, Philippines, or Southern Europe; 2x more likely with Mountains or Desert Mountains terrain.

| Severity | Characters killed | Supply Limit | Construction Time | Monthly Control | Popular Opinion | Danger | Plague Resistance |
|---|---|---|---|---|---|---|---|
| 1 | 5% | −40% | +30% | −0.2 | −20 | +20 | −3 |
| 2 | 10% | −50% | +40% | −0.4 | −25 | +30 | −6 |
| 3 | 15% | −60% | +50% | −0.6 | −30 | +40 | −9 |

### Flood

Occurs only in counties adjacent to major rivers, 2x more likely with Farmlands or Plains. Always severity 2-3 if flooding the Nile or Yellow River.

| Severity | Characters killed | Supply Limit | Construction Time | Monthly Control | Popular Opinion | Danger | Plague Resistance |
|---|---|---|---|---|---|---|---|
| 1 | 5% | −60% | +60% | −0.6 | −20 | +20 | −9 |
| 2 | 10% | −70% | +70% | −0.8 | −25 | +30 | −12 |
| 3 | 15% | −80% | +80% | −1 | −30 | +40 | −15 |

### Character Death in Situations

If the player character is selected for death, both the player and their primary heir are at risk. Choose:

- Try to survive together (twice as difficult Prowess challenge; both wounded; one dies on failure)
- Try to survive separately (individual Prowess challenges; losers die)
- Sacrifice yourself (player dies, family member survives unharmed, dynasty gains 250 Renown)
- Sacrifice family member (family member dies, player survives, lose 350 Prestige, 250 Piety, gain Craven trait)

## Dynastic Cycle (requires Royal Court)

Present in all start dates, the Dynastic Cycle affects the Hegemony of China. Characters become interlopers if they own de jure China territory or hold a China barony currently owned by the hegemon. They become involved if they are part of China or a tributary with Palace Access.

### Eras

The Cycle alternates between Tension and either Advancement or Expansion (starting 1066 in Advancement, 867/1178 in Tension; 867 starts 40% toward Division). The Hegemon selects Favored Era every 20 years for 250 Influence. When Advancement/Expansion begins, spend 225 Legitimacy and 50 opinion with movement members to switch eras.

Every 10 years, the Hegemon or movement members add 50 Catalyst Progress for 250 Influence and 200 movement Power (Pro-Dynasty if Hegemon).

### Advancement Era

**Effects:** Tributary Imperial Grace −1/year, +1 Integrate Title councilor progress.

**Hegemon effects:** Unlocks Metropolitan administration, Efficient Governance variant, General Secretariat Control law, building construction in tributaries (no war declaration), +20% Cultural Fascination, −15% Building/Great Projects Construction Cost, −2 Max Men-at-Arms Regiments, +1-2 Expected Legitimacy Level (50-100 years).

**Catalysts:** +50 Religious Uniformity/Census/Sinicize completed; +35 yearly if Favored; +25 if Advancement gains Power; +20 if Legitimacy Celestial/Pro-Dynasty Favored; +10 secret exposed/hook gained; −10-15 Expansion favored/non-councilor contributed/new Hegemon different house.

### Expansion Era

**Effects:** Tributary Imperial Grace −2/year, no Integrate Title task, vassals with different government can declare internal wars.

**Hegemon effects:** Unlocks Seize Hegemonic County/Duchy casus bellis, Protectorate administration, Grand Expansionist Command law, Military Strategists variant, +2 Max Title Men-at-Arms Regiments, +50 Legitimacy per conquered Duchy/Kingdom, +20% Court Position Salary.

**Catalysts:** +50 Grand Campaign/Great Wall extensions/Military Exercise completed; +35 yearly if Favored; +25 if Expansion gains Power; +10 non-councilor Great Wall/wall contributed.

### Tension Era

**Effects:** Tributary Imperial Grace −3/year, no Integrate Title task (Military Admin unlocks Seize), vassals likely internal wars, non-jure subjects likely independence, factions more likely, Populist/Peasant double Discontent, −5% Governor Efficiency per legitimacy below 5, −100 Legitimacy per disaster.

**Hegemon effects:** Cannot declare war, offer vassalage, or increase authority law; +20% Legitimacy gain/loss, −20 Vassal Opinion, −20% Vassal Treasury.

### Conquest Era

Same Tributary Imperial Grace −3 and Seize casus bellis as Tension. **Hegemon effects:** Unlocks Promote Cultural Governors decision, +2 Max Title Men-at-Arms Regiments, −30% Mercenary Cost, +50 Legitimacy per conquest, +20% Legitimacy gain/loss, −100 per disaster, −20 Vassal Opinion, −20% Vassal Treasury, all tributaries become independent.

### Division

Reached via Catalysts during Tension/Conquest, <30% de jure control, Illegitimate Ruler legitimacy, or Hegemony destruction. All Hegemony titles held by China ruler destroyed; former Hegemon suffers succession; all subjects become independent. Kingdom/Empire titles destroyed if holders have <100/350 Movement Power. Silk Road enters Hardship; Attend Children's Examination unavailable.

Interlopers gain −20% Taxes, +100% Great Project Legitimacy, gain Legitimacy for Merit 1-4 appointments, unlock Consolidate Land Under Heaven casus belli. Claim the Mandate of Heaven with >50% de jure counties to immediately gain Hegemony title, 1000 Treasury, 1000 Influence, 2500 Renown, 25 Control, Maximum Legitimacy, vassal tributaries, Celestial government, and vassal non-Republic/Theocracy vassals. Courtiers with 3000+ Merit create noble families; replace councilors with higher Merit Rank ones. Son of Heaven modifier granted. Choose phase: Advancement or Expansion.

### Political Movements

All China subjects divided among four movements: Pro-Dynasty, Advancement, Expansion, Conservative, Unaligned. Change every 5 years for 250 Influence. Personal Movement Power increases via age, title rank, Merit rank, devotion, influence, men-at-arms, Governor experience, estate upgrades, disciples, council positions, diarch status.

Movement Power 800+ unlocks Dismiss Hook, Request Raid Permission, Raid Estate scheme. Leaders unlock Make Movement Petition; replace via death or debate loss. Movements grant era-specific effects.

## The Silk Road (requires Royal Court)

Affects rulers with capitals in Silk Road regions. Six regions: Occident < Transcaspia/India < Central Asia/Tibet < China, connected west-to-east. Each region has assigned innovations; every 12 years Han innovations rotate west. Cultures with Chinese heritage or Sinophilic tradition can research normally; others unlock via Market visit (skill check).

| Phase/Participant | Hardship | Steady Trading | Exceptional Bounty |
|---|---|---|---|
| Everyone | −2% Development Growth | +1% Dev Growth, +2% Cultural Fascination, −5 Plague Resistance | +2% Dev Growth, +5% Cultural Fascination, −10 Plague Resistance |
| Lands Under Heaven | +10% Legitimacy Loss | +1% Domain Taxes | +2% Domain Taxes |
| Silk Road Domains | −2% Domain Taxes | +1% Domain Taxes | +2% Domain Taxes, +0.01 Monthly Dev |
| Silk Road Realms | −1% Domain Taxes | None | +2% Domain Taxes |
| Peripheral Realms | −1% Domain Taxes | None | +1% Domain Taxes |
| Steppe Nomads | +2% County Fertility Growth | +0.5% Herd Conversion to Horde Riders | +0.7% Herd Conversion, +10% Move Domicile Speed, −2% Fertility Growth |

**Catalysts:** +30 Grand Canals (China), +20 (Central Asia/Tibet), +10 (India/Transcaspia), +15 Bazaars, +15 yearly peace, +10 adjacent upstream peace, +5 Stability phase, +15 Iranian Intermezzo ends, −5-15 wars, −10 raid, −15 siege by Greatest Khans, −50 Byzantine Empire destroyed, −3 yearly Iranian Unrest.

## Steppe Seasons

Affects Nomadic government characters in specific regions when The Great Steppe game rule enabled. Highest-herd character becomes Gurkhan (Unrestricted Dominance law, Establish Paiza System decision).

Five season situations cover multiple regions:

| Situation | Regions | Seasons available |
|---|---|---|
| The Great Steppe | Central/Eastern/Western Steppe | All 7 |
| Changthang | Eastern/Western Plateau, River Valley | Everlasting Summer through Cold Zud |
| The Taiga and Tundra | Karelia, Sápmi | Everlasting Summer through Cold Zud |
| Al-Bādiya | Egypt, Arabian Desert | Everlasting Summer through Severe Drought |
| Bilād as-Sūmāl | Horn of Africa, Nubia | Everlasting Summer through Severe Drought |
| Tiniri | North Africa, Sahara, Sahel | Everlasting Summer through Severe Drought |

Seasons change every 10 years and are visible on the map. Nomads view affected regions and are fully affected. Predict seasons via Stargazer court position (accuracy by Aptitude).
