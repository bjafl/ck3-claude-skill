---
title: Council
category: realm-and-succession
tags: [council, government, vassals]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Council]
---

A council consists of specialized vassals or courtiers who help a landed ruler govern their realm. Councilors assigned to tasks cannot simultaneously lead troops in battle. Progress on most councilor tasks is preserved when switching tasks, except for Integrate Title and Increase Development/Control in County, though progress continues even if the councilor dies. Task effects scale linearly with councilor skill, and relationship modifiers (Friend/Best Friend/Rival/Nemesis) adjust efficiency by 20-30%.

## Task Mechanics

Councilor tasks can trigger one related event per year, prohibited in the first month of assignment. Positive events occur when skill exceeds 8, negative events when skill is below 15. Characters with the Incapable trait cannot be appointed councilors.

Efficiency multipliers based on relationship with liege:
- Friend: +20%
- Best Friend: +30%
- Rival: -20%
- Nemesis: -30%

## Spymaster

Handles schemes and counter-espionage using Intrigue as primary skill. In the Celestial Hegemony of China, this position becomes Imperial Censor with the Censorate title. Three possible tasks:

| Task | Effects | Possible positive events | Possible negative events |
|---|---|---|---|
| Disrupt Schemes | +5 Days Enemy Hostile Scheme Phase Length (Base) +0.5 Days Enemy Hostile Scheme Phase Length per Councilor Skill +1% Scheme Discovery Chance per Councilor Skill | Hostile Scheme Disrupted | Courtier's Secret Revealed Your Secret Revealed |
| Support Schemes | -1 Days Hostile Scheme Phase Length per Councilor Skill +5% Hostile Scheme Success Chance (Base) +0.5% Hostile Scheme Success Chance per Councilor Skill | Secret Discovered | Loss of Piety Loss of Prestige Scheme Failure |
| Find Secrets | +5% Chance to discover a Secret at court (if any) per Councilor Skill With Truth is Relative perk, a Hook will be fabricated if there are no Secrets | None | Find Secrets Discovered |

## Confidant

A position occupied automatically (in order: vizier, then primary spouse if unlanded or direct vassal) and unavailable in the Celestial Hegemony. No negative effects from low skill. Six possible tasks:

| Task | Effects | Possible positive events |
|---|---|---|
| Assist Ruler | 20% of all Councilor's Skills are added to the Ruler's |  |
| Court Politics | 50% of Councilor's Diplomacy Skill added to Ruler's +0.75% monthly chance for +1 Diplomacy modifier (may become Diplomat trait after 2 gains) | Gain Opinion with family member Two children stop being rivals Player Heir befriends a sibling Confidant loses Shy trait or gains Gregarious trait |
| Chivalry | 50% of Councilor's Martial Skill added to Ruler's +0.75% monthly chance for +1 Martial modifier (may become Strategist trait after 2 gains) | Gain Dread Gain Prestige Gain a health boost Gain additional levies A child gains Prowess |
| Manage Domain | 50% of Councilor's Stewardship Skill added to Ruler's +0.75% monthly chance for +1 Stewardship modifier (may become Architect trait after 2 gains) | Gain Gold Gain Prestige Gain opinion with a courtier Gain a health boost Gain a Weak Hook on a courtier A county gains Development |
| Court Intrigue | 50% of Councilor's Intrigue Skill added to Ruler's +0.75% monthly chance for +1 Intrigue modifier (may become Schemer trait after 2 gains) | Gain opinion with the spymaster Uncover a scheme Uncover a vassal's secret Gain a Weak Hook on a courtier or vassal |
| Patronage | 50% of Councilor's Learning Skill added to Ruler's +0.75% monthly chance for +1 Learning modifier (may become Scholar trait after 2 gains) | Gain Piety Gain opinion with head of faith Gain opinion with a zealous vassal Someone converts to the character's faith Someone converts to the character's culture Children in court gains progress for better education trait |

## Regular Council

Standard rulers (those without Nomadic government or Celestial Hegemony status) have four additional council positions: Chancellor, Steward, Marshal, and Religious Affairs Councilor.

### Chancellor

Diplomacy-focused position with four tasks:

| Task | Effects | Possible positive events | Possible negative events | Requirements |
|---|---|---|---|---|
| Foreign Affairs | +0.05 Prestige per Councilor Skill +0.5 Independent Ruler Opinion per Councilor Skill | Shorten Truce | Enemy Claim Neighbor Opinion Loss Shorten Enemy Truce |  |
| Domestic Affairs | +0.5 Direct Vassal Opinion per Councilor Skill (+0.2/month until max) +0.5 Direct Parochial Opinion per Councilor Skill (+0.2/month until max) +1% Tyranny Loss per Skill | End Internal War Force Partition for Vassal Improved Feudal Contract Increase Vassal Opinion | Lowered Vassal Opinion Worsened Feudal Contract |  |
| Integrate Title | At 100% progress, the targeted title becomes de jure part of the Primary Title | Task Boost | Task Setback | Any county in realm currently de jure drifting |
| Bestow Royal Favor | +0.5 Vassal Prestige +0.02 Prestige per Councilor Skill +0.5 Vassal Opinion per Councilor Skill | End Internal War Increase Vassal Opinion | Lowered Vassal Opinion Worsened Feudal Contract | (requires Royal Court) Court Grandeur level 2 or higher |

### Steward

Stewardship-based position with five tasks:

| Task | Effects | Possible positive events | Possible negative events | Requirements |
|---|---|---|---|---|
| Collect Taxes | +0.5% Domain Taxes per Councilor Skill | Extra Taxes | County Corruption |  |
| Increase Development in County | −1.25% Building and Holding Construction Time per Councilor Skill +0.175 Monthly Development Growth per Councilor Skill At 100% increase Development by 1 | Efficient Taxation Increased Control | Loss of Control Loss of Opinion Slow Construction | County development < 100 |
| Promote Culture | Base speed (0.25 + councilor skill ÷ 20)% per month. At 100%, county changes culture to the liege's. | Improve County Opinion Increased Levies Increased Taxes | Loss of County Opinion Resistance to Settlers | County culture is different from liege |
| Promote Cultural Acceptance | +0.01 Cultural Acceptance per Councilor Skill +0.05 Cultural Acceptance per Councilor Skill if Independent | Cultural Acceptance Boost Increased Development Growth Increased Opinion | Reduced Development Growth | Duke or higher Realm County with different culture and culture acceptance < 100% with liege's culture |
| Convince De Jure Territory | Base speed (0.1 + councilor skill ÷ 20)% per month. At 100%, the ruler of the target county hands it over to its de jure liege. | Prestige Gain | Prestige Loss Diplomatic Blunder | (requires Royal Court) Court Grandeur level 6 or higher Any county: De jure of top title County holder has a different top liege |

### Marshal

Martial-focused position with four tasks:

| Task | Effects | Possible positive events | Possible negative events | Requirements |
|---|---|---|---|---|
| Organize Army | −1% Raised Army Maintenance per Councilor Skill +2% Levy Reinforcement Rate per Councilor Skill +2% Garrison Size per Councilor Skill | Increased Military Presence Well-organized Service | Insufficient Guards Levy Desertion Unused Farmland |  |
| Train Commanders | +1% Knight Effectiveness per Councilor Skill (+1%/month until max) +1% Men-at-Arms Damage per Councilor Skill (+1%/month until max) +1% Men-at-Arms Toughness per Councilor Skill (+1%/month until max) +0.5% Monthly chance to improve or find a Commander/Knight per Councilor Skill | Commander Gains Commander Trait Knight improved | Commander Killed Commander Maimed Commander Wounded |  |
| Increase Control in County | +0.2% Monthly chance to remove County Corruption per Councilor Skill Targeted County cannot gain Corruption | Baron Opinion Increase Increase County Opinion | Baron Opinion Loss Lose County Opinion Loss of Control | A county with Corruption or less than 100 Control |
| Manage Royal Guards | +2% Knight Effectiveness per Councilor Skill −2% Enemy Hostile Scheme Success Chance per Councilor Skill | Knight Improved Hostile Scheme Disrupted | Disorganized Royal Guards Knight Wounded | (requires Royal Court) Court Grandeur level 3 or higher |

### Religious Affairs Councilor

Two variants exist based on faith doctrine: Court Chaplain (Lay Clergy) and Realm Priest (Theocratic). Both use Learning as primary skill. Appointment follows faith's Clerical Appointment doctrine; appointees must share liege's faith and be allowed by Clerical Gender doctrine. Excommunicated characters cannot be appointed if faith has Communion tenet, unless liege is also excommunicated.

Realm Priest specifically leases all Temple holdings in liege's domain and receives taxes/levies from vassal Realm Priests of the same faith, ranging from 0-50 based on Opinion (all taxes/levies granted regardless of Opinion if liege has Strong Hook).

Three possible tasks:

| Task | Effects | Possible positive events | Possible negative events | Requirements |
|---|---|---|---|---|
| Religious Relations | +0.05 Monthly Piety per Councilor Skill +0.5 Same Faith Theocratic Ruler Opinion per Councilor Skill (+0.35/month until max) | Increase Vassal Opinion | Loss of Piety Loss of Vassal Opinion |  |
| Fabricate Claim on County | Base speed (3 + councilor skill ÷ 5)% per month. At 100%, gain an unpressed claim. | Claim on Duchy | Loss of Piety Upset Target Vassal Opinion Loss |  |
| Convert Faith in County | Base speed (0.5 + councilor skill ÷ 10)% per month. At 100%, county changes faith to the liege's. | Increase County Development Increase County Levies Increase County Opinion | Loss of County Opinion Resistance to Conversion | Realm county with different faith |

## Kurultai

Nomadic government rulers can grant four Kurultai positions whose obedience is necessary for stable succession. Eight possible tasks:

| Task | Primary skill | Effects | Possible positive events | Possible negative events | Requirements |
|---|---|---|---|---|---|
| Domestic Affairs | Diplomacy | +0.5 Direct Vassal Opinion per Councilor Skill (+0.2/month until max) +0.5 Direct Parochial Opinion per Councilor Skill (+0.2/month until max) +1% Tyranny Loss per Skill | End Internal War Force Partition for Vassal Improved Feudal Contract Increase Vassal Opinion | Lowered Vassal Opinion Worsened Feudal Contract | Can only be done by one councilor |
| Support Herders | Diplomacy | +0.5% Herd Gain per Councilor Skill +0.5% Herd Capacity per Councilor Skill | Gain Horde Rider Army Increase Herd Size | Decrease Herd Size Loss of Control |  |
| Increase Control in County | Martial | +0.2% Monthly chance to remove County Corruption per Councilor Skill Targeted County cannot gain Corruption | Baron Opinion Increase Increase County Opinion | Baron Opinion Loss Lose County Opinion Loss of Control |  |
| Organize Raiders | Martial | +1% Max Loot per Councilor Skill +0.5% Raid Speed per Councilor Skill +0.5% Movement Speed while Raiding per Councilor Skill -1% Hostile County Attrition while Raiding per Councilor Skill | Gain Dread Gain Prestige | Loss Dread Lose Prestige | Can only be done by one councilor |
| Exploit Lands | Stewardship | +1% Gold from Herd per Councilor Skill +0.03% County Fertility per Councilor Skill | Gain Dread Gain Gold | Lose county Opinion Reduce Fertility | County must not be targeted by another task County must be in domain |
| Manage Fertility | Stewardship | +1% County Fertility per Councilor Skill | Increase County Opinion Increase Fertility | Prestige Loss Reduce Fertility | County must not be targeted by another task |
| Aid Stargazer | Learning | +0.2% Piety Gain per Councilor Skill +0.2 Stargazer Aptitude per Councilor Skill | Gain Piety Gain Stargazer Opinion | Lose Piety Lose Stargazer Opinion |  |
| Explore Cultures | Learning | -0.08% Culture Reformation Cost per Councilor Skill -0.08% Culture Reformation Cooldown per Councilor Skill -0.08% Culture Hybridizing Threshold per Councilor Skill | Gain Cultural Acceptance Gain Different Culture Opinion | Lose Cultural Acceptance Lose Different Culture Opinion | Can only be done by one councilor |

## Hegemony of China Council

The Celestial Hegemony of China grants 8 additional council positions with unique benefits. Councilors receive a salary managed through realm budget allocation, with domicile always at realm capital. Additional bonuses include:

- Interactions with fellow vassals
- Titular Empire title
- +1 Max Hostile, Personal and Political schemes
- +8 Monthly Influence
- Can be given Favored Minister position
- Unlock Department Aide position
- Can take Request Bestowal of Honors decision
- (requires Khanate) Grant Examination Exemption option (600 Influence) for automatic examination passes; multiple uses cost 2000 Merit each

Celestial councilors cannot hold landed titles (triggers succession if appointed while holding any). Their claims cannot be used in casus belli. When a councilor dies, replacement is automatic from characters with Merit Rank 3+ with highest score. Score components:

- +100 if movement leader
- +100 if same culture as liege and liege took Promote Cultural Governors decision
- +25 if favored movement
- +20 if Elder of current councilor
- +10 if Disciple of current councilor
- +10 if age above 40
- +10 per level of Influence
- +1 per skill used by position
- -5 if age below 30
- All bonuses reduced by 75% if older than retirement age
- All bonuses reduced by 80% if not favored by gender law

### Hegemon Interactions

- Request Mentorship: Choose a courtier. Councilor gains +30 Merit; courtier becomes Disciple. Councilor can grant the Disciple Merit, a commander trait, or Confucian Education trait.
- Requisition Treasury: Take up to half councilor's Treasury (max 400 per councilor title rank). Costs 30 Influence +10 per Merit Rank of councilor. Refusal costs 60 Influence +30 per level of Merit lower than liege.
- Request Commander: (Minister of War only) Select a courtier of the councilor to add to hegemon's court. Costs 55 Treasury; courtier must be adult, eligible for commander role, and not close family.

### Departments

Departments are the 3 most powerful councilors; one is designated as diarch by Grand Secretariat Control law. Spymaster also qualifies as department (called Imperial Censor).

**Grand Chancellor** (Diplomacy):
- Foreign Affairs: +0.05 Prestige per Councilor Skill +0.5 Independent Ruler Opinion per Councilor Skill | Positive: Shorten Truce | Negative: Enemy Claim Neighbor Opinion Loss Shorten Enemy Truce | Unlocks: Consult Heaven decision Shape the Dynastic Cycle decision Summon Courtiers for the Celestial Bureau decision Compel Religious Uniformity great project
- Domestic Affairs: +0.5 Direct Vassal Opinion per Councilor Skill (+0.2/month until max) +0.5 Direct Parochial Opinion per Councilor Skill (+0.2/month until max) +1% Tyranny Loss per Skill | Positive: End Internal War Force Partition for Vassal Improved Feudal Contract Increase Vassal Opinion | Negative: Lowered Vassal Opinion Worsened Feudal Contract | Unlocks: Consult Heaven decision Shape the Dynastic Cycle decision Summon Courtiers for the Celestial Bureau decision Compel Religious Uniformity great project
- Integrate Title: At 100% progress, targeted title becomes de jure part of Primary Title | Positive: Task Boost | Negative: Task Setback | Unlocks: Consult Heaven decision Shape the Dynastic Cycle decision Summon Courtiers for the Celestial Bureau decision Compel Religious Uniformity great project

**Grand Marshal** (Martial):
- Train Commanders: +1% Knight Effectiveness per Councilor Skill (+1%/month until max) +1% Men-at-Arms Damage per Councilor Skill (+1%/month until max) +1% Men-at-Arms Toughness per Councilor Skill (+1%/month until max) +0.5% Monthly chance to improve or find a Commander/Knight per Councilor Skill | Positive: Commander Gains Commander Trait Knight improved | Negative: Commander Killed Commander Maimed Commander Wounded | Unlocks: Dynasty's Grand Campaign great project Construct Great Barracks great project Liege's conquest CBs Title men-at-arms
- Lead Troops: +0.2 Advantage per Councilor Skill −0.25% Friendly Fatal Casualties per Councilor Skill +0.25% Enemy Fatal Casualties per Councilor Skill | Unlocks: Dynasty's Grand Campaign great project Construct Great Barracks great project Liege's conquest CBs Title men-at-arms

### Ministries

Ministries are the 6 less powerful councilors with various interactions and responsibilities:

**Minister of Personnel** (Diplomacy):
- Manage Talent: +1% Yearly chance to gain a skilled courtier in a court position per Councilor Skill +0.25 Courtier and Guest Opinion per Councilor Skill | Fellow vassal interactions: Request Retirement Demand Courtier
- Bestow Royal Favor: +0.5 Vassal Prestige +0.02 Prestige per Councilor Skill +0.5 Vassal Opinion per Councilor Skill | Positive: End Internal War Increase Vassal Opinion | Negative: Lowered Vassal Opinion Worsened Feudal Contract | Fellow vassal interactions: Request Retirement Demand Courtier

**Minister of War** (Martial):
- Organize Army: −1% Raised Army Maintenance per Councilor Skill +2% Levy Reinforcement Rate per Councilor Skill +2% Garrison Size per Councilor Skill | Positive: Increased Military Presence Well-organized Service | Negative: Insufficient Guards Levy Desertion Unused Farmland | Fellow vassal interactions: Have a Governor Join War Debt Relief (Military governors)
- Increase Control in County: +0.2% Monthly chance to remove County Corruption per Councilor Skill Targeted County cannot gain Corruption | Positive: Baron Opinion Increase Increase County Opinion | Negative: Baron Opinion Loss Lose County Opinion Loss of Control | Fellow vassal interactions: Have a Governor Join War Debt Relief (Military governors)
- Manage Royal Guards: +2% Knight Effectiveness per Councilor Skill −2% Enemy Hostile Scheme Success Chance per Councilor Skill | Positive: Knight Improved Hostile Scheme Disrupted | Negative: Disorganized Royal Guards Knight Wounded | Fellow vassal interactions: Have a Governor Join War Debt Relief (Military governors)

**Minister of Revenue** (Stewardship):
- Collect Taxes: +0.5% Domain Taxes per Councilor Skill | Positive: Extra Taxes | Negative: County Corruption | Fellow vassal interactions: Requisition Treasury Debt Relief (Civilian governors)
- Promote Culture: At 100% County changes Culture to the liege's | Positive: Improve County Opinion Increased Levies Increased Taxes | Negative: Loss of County Opinion Resistance to Settlers | Fellow vassal interactions: Requisition Treasury Debt Relief (Civilian governors)
- Promote Cultural Acceptance: +0.01 Cultural Acceptance per Councilor Skill +0.05 Cultural Acceptance per Councilor Skill if Independent | Positive: Cultural Acceptance Boost Increased Development Growth Increased Opinion | Negative: Reduced Development Growth | Fellow vassal interactions: Requisition Treasury Debt Relief (Civilian governors)
- Convince De Jure Territory: The target County requires its ruler to hand it over to its De Jure liege | Positive: Prestige Gain | Negative: Prestige Loss Diplomatic Blunder | Fellow vassal interactions: Requisition Treasury Debt Relief (Civilian governors)

**Minister of Works** (Stewardship):
- Increase Development in County: −1% Building and Holding Construction Time per Councilor Skill +0.175 Monthly Development Growth per Councilor Skill At 100% increase Development by 1 | Positive: Efficient Taxation Increased Control | Negative: Loss of Control Loss of Opinion Slow Construction | Fellow vassal interactions: Can build in realm
- Support Great Projects: −0.5% Great Project Construction Time per Councilor Skill | Positive: Extra Taxes | Negative: County Corruption | Fellow vassal interactions: Can build in realm

**Minister of Rites** (Learning):
- Religious Relations: +0.05 Monthly Piety per Councilor Skill +0.5 Same Faith Theocratic Ruler Opinion per Councilor Skill (+0.35/month until max) | Positive: Increase Vassal Opinion | Negative: Loss of Piety Loss of Vassal Opinion | Fellow vassal interactions: Compel Conversion
- Convert Faith in County: At 100% county changes faith to the liege's | Positive: Increase County Development Increase County Levies Increase County Opinion | Negative: Loss of County Opinion Resistance to Conversion | Fellow vassal interactions: Compel Conversion
- Explore Cultures: -0.08% Culture Reformation Cost per Councilor Skill -0.08% Culture Reformation Cooldown per Councilor Skill -0.08% Culture Hybridizing Threshold per Councilor Skill | Positive: Gain Cultural Acceptance Gain Different Culture Opinion | Negative: Lose Cultural Acceptance Lose Different Culture Opinion | Fellow vassal interactions: Compel Conversion

**Minister of Justice** (Learning):
- Fabricate Claim on County: At 100% gain an Unpressed Claim | Positive: Claim on Duchy | Negative: Loss of Piety Upset Target Vassal Opinion Loss | Fellow vassal interactions: Imprison Grant Pardon
- Justify Rule: −0.1 Yearly Tyranny Loss +0.2% Legitimacy Gain | Fellow vassal interactions: Imprison Grant Pardon

## Councilor Benefits by Title Rank

Each councilor receives benefits based on position and liege's title rank, scaled appropriately:

| Council position | County | Duchy | Kingdom | Empire | Hegemony |
|---|---|---|---|---|---|
| Spymaster | +10 Natural Dread +5% Scheme Secrecy +5% Intrigue Lifestyle Experience | +20 Natural Dread +10% Scheme Secrecy +10% Intrigue Lifestyle Experience | +30 Natural Dread +15% Scheme Secrecy +15% Intrigue Lifestyle Experience | +40 Natural Dread +20% Scheme Secrecy +20% Intrigue Lifestyle Experience | +50 Natural Dread +25% Scheme Secrecy +25% Intrigue Lifestyle Experience |
| Marshal/Grand Marshal/Minister of War | +1 Prowess −5% Army Maintenance +5% Levy Size +5% Martial Lifestyle Experience | +2 Prowess −10% Army Maintenance +10% Levy Size +10% Martial Lifestyle Experience | +3 Prowess −15% Army Maintenance +15% Levy Size +15% Martial Lifestyle Experience | +4 Prowess −20% Army Maintenance +20% Levy Size +20% Martial Lifestyle Experience | +5 Prowess −25% Army Maintenance +25% Levy Size +25% Martial Lifestyle Experience |
| Chancellor/Grand Chancellor/Minister of Justice/Minister of Personnel | Scaled Prestige +5 Fellow Vassal Opinion +5% Diplomacy Lifestyle Experience | Scaled Prestige +10 Fellow Vassal Opinion +10% Diplomacy Lifestyle Experience | Scaled Prestige +15 Fellow Vassal Opinion +15% Diplomacy Lifestyle Experience | Scaled Prestige +20 Fellow Vassal Opinion +20% Diplomacy Lifestyle Experience | Scaled Prestige +25 Fellow Vassal Opinion +25% Diplomacy Lifestyle Experience |
| Steward/Minister of Revenue/Minister of Works | Scaled Gold +2.5% Domain Taxes −2.5% Building Construction Cost +5% Stewardship Lifestyle Experience | Scaled Gold +5% Domain Taxes −5% Building Construction Cost +10% Stewardship Lifestyle Experience | Scaled Gold +7.5% Domain Taxes −7.5% Building Construction Cost +15% Stewardship Lifestyle Experience | Scaled Gold +10% Domain Taxes −10% Building Construction Cost +20% Stewardship Lifestyle Experience | Scaled Gold +12.5% Domain Taxes −12.5% Building Construction Cost +20% Stewardship Lifestyle Experience |
| Court Chaplain/Realm Priest/Minister of Rites | Scaled Piety +5 Popular Opinion +5% Learning Lifestyle Experience | Scaled Piety +10 Popular Opinion +10% Learning Lifestyle Experience | Scaled Piety +15 Popular Opinion +15% Learning Lifestyle Experience | Scaled Piety +20 Popular Opinion +20% Learning Lifestyle Experience | Scaled Piety +25 Popular Opinion +25% Learning Lifestyle Experience |
| (requires Khans of the Steppe) Kurultai | Scaled Gold +0.15 Monthly Prestige +5% Herd Gain +5% Herd Capacity | Scaled Gold +0.3 Monthly Prestige +10% Herd Gain +10% Herd Capacity | Scaled Gold +0.45 Monthly Prestige +15% Herd Gain +15% Herd Capacity | Scaled Gold +0.6 Monthly Prestige +20% Herd Gain +20% Herd Capacity | Scaled Gold +0.75 Monthly Prestige +25% Herd Gain +25% Herd Capacity |
