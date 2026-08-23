---
title: Casus Belli
category: warfare
tags: [war, casus belli, claims, conquest, holy war, subjugation]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Casus_belli]
---

A casus belli (cause for war) is a formal justification required to declare war. Without one, characters cannot declare war. Wars only yield what the casus belli specifies, and wars end if the casus belli's conditions are no longer met. Casus belli costs can be paid with Prestige or Piety (or Fame/Devotion levels if unable to pay). Declaring war on a Head of Faith costs 500 Piety (spiritual) or 100 Piety (temporal), plus 100 additional Piety if attacking a same-faith theocracy. War targets are map regions that give bonus war score when occupied; if unspecified, the defender's capital becomes the war target.

## Independence Wars

Feudal, Clan, Tribal, Wanua, Nomadic, Mandala, and Sōryō subjects can declare independence wars (100 Prestige vs. suzerain, 500 vs. liege; Tribal government pays half). These also trigger if Independence factions' ultimatums are refused.

Outcomes:
- Enforcing demands: attacker becomes independent
- White peace: attacker remains subject; tributaries get reduced obligations
- Surrender: attacker remains subject; vassals get imprisoned (defender gains revocation reason); tributaries get increased obligations and -20 Dread to defender

## Claims Wars

Claims wars target titles held by the attacker, or by their vassals or courtiers (guests must be invited to court). Initially one title can be claimed, but Divine Right innovation or Heroic Bloodline legacy 2 (personal), or Rightful Ownership innovation (vassal/courtier) allow multiple titles.

Outcomes:
- Enforcing demands: claimant gains titles; liege gains weak hook; courtiers become vassals; if new rank equals/exceeds liege's, become independent
- White peace: defender keeps titles; contested unpressed claims become pressed
- Surrender: defender keeps titles; claims used in war are lost

Base Prestige costs by title rank:

| Title | Own Claim | Dynasty Claim | Other's Claim |
|-------|-----------|---------------|---------------|
| County | 100 | 250 | 500 |
| Duchy | 200 | 500 | 1000 |
| Kingdom | 400 | 1000 | 2000 |
| Empire | 800 | 3000 | 6000 |

Own claim cost modifiers:
- -50% same dynasty
- -50% defender is child, attacker is not
- -25% if claim is pressed
- -25% same faith and defender's gender unfavored while attacker's is favored
- +25% same faith and defender's gender favored while attacker's is not
- +25% different faith
- +25% defender's rank lower than attacker's
- +50% attacker is child, defender is not
- +1000% attacker is adventurer

Other claims cost modifiers:
- +25% claimant different house, same dynasty
- +50% claimant different dynasty
- +100% claimant different religion

## Conquest Wars

Cost is Piety if target has same faith, Prestige otherwise.

Outcomes:
- Enforcing demands: attacker gains title and fame equal to war contribution share
- White peace: defender keeps title; attacker loses 75-100 Prestige
- Surrender: defender keeps title; attacker pays gold and gains +25 faction discontent

Conquest war types by target and requirement:

| Target | Fame | Cost | Contribution | Limit | Requirements |
|--------|------|------|--------------|-------|--------------|
| County | Established | 2.5/5/10 per realm size (by gov) | 75 | Unlimited | Clan/Tribal/Admin/Nomadic/Sōryō/Wanua gov OR unreformed faith OR Warmonger/Pursuit of Power tenet OR Quarrelsome tradition |
| Duchy | Illustrious | 6/10/20 per realm size | 150 | Unlimited | Clan/Tribal/Nomadic/Wanua gov OR unreformed/Warmonger/Pursuit of Power OR Quarrelsome OR (Frontier/Naval vassal + adjacent) OR Rulers of the Black Sea modifier |
| Kingdom | Exalted Among Men | 100/1000/2000 (varies) | 350 | Varies by house unity | Clan/Tribal/Nomadic/Wanua OR unreformed/Warmonger/Pursuit of Power |
| Empire | Established | 200 | 350 | Unlimited | Admin + conquered Roman Empire county (Abbadan, Alexandria, Antiocheia, Bari, Byzantion, Chandax, Cumberland, Edessa, Jerusalem, Lombardia, Murcia, Northumberland, Ravenna, Roma, Siracusa, Tangiers, Touraine, Trier, Tunis) |
| Hegemony | Established | 2000 | 350 | Unlimited | Involved in Dynastic Cycle targeting Hegemony of China |

### Struggle Clash

Available to rulers in Iberian Struggle or with Dominance ending. Targets adjacent defender counties in struggle region. Costs vary by phase:

| Phase | Targets | Cost |
|-------|---------|------|
| Opportunity | Any | 150 per county |
| Hostility | Any | 75 per county |
| Conciliation/Compromise | One | 350 per county |

### Adventurer Invasion Wars

Only for adventurers, requires sponsor rank (if sponsored). Additional 250 Piety if defender shares faith.

| Target | Fame | Cost |
|--------|------|------|
| County | Established | 500 Prestige |
| Duchy | Illustrious | 2000 Prestige |
| Kingdom | Exalted Among Men | 5000 Prestige |
| Empire | The Living Legend | 10000 Prestige |

On victory, adventurer gains defender's government type and gold scaling with camp size.

### Other Conquest CBs

- **Ducal Conquest**: Perk-gated, targets counties in uncreated duchy; 350 Prestige (Count) or 750 (higher)
- **Laudably Conquer County**: House modifier, targets Irish counties; 50 Prestige (different faith) or 25 Piety (same faith)
- **Iberian Reclamation**: Iberian Struggle Hostility/Conciliation phases; targets one duchy at 75 base + 25 per county
- **Mediterranean Conquest**: House modifier, Mediterranean coast counties; 300 Prestige
- **[Roads to Power] Seize Peripheral Duchy**: Non-Admin rulers vs. Admin kings+; duchy not de jure part of attacker's title; expanded options if target in civil war
- **[Khans of the Steppe] Overrun Duchy/Kingdom**: Independent rulers with Dominance law; new capital gains attacker's faith/culture; attacker's tributaries become independent; conquered counties lose 1-4 development
- **[Khans of the Steppe] Greatest of Khans' Onslaught**: Story event, no cost, all target titles; conqueror's capital (if held), government, and tributaries change
- **Seize Hegemonic County/Duchy**: Hegemon of China and Grand Marshal during Expansion/Conquest cycle, adjacent targets
- **Imperial County Pacification**: Ritsuryō government with Imperial Pacification law, Japanese counties; 190 base cost
- **Grand Campaign**: Dynasty great project, Hegemony of China; 200 Legitimacy + 100 Movement Power on victory

## De Jure Wars

Higher-title holders can declare de jure wars on lower-title holders not already vassals (100 Prestige per county, 300 prestige war contribution share). Can target one County/Duchy normally; Divine Right innovation allows all titles at once. Roman Empire owners ignore de jure boundaries for ancient Roman duchies (no cost).

Outcomes:
- Enforcing demands: attacker gains title; liege gains weak hook if vassal
- White peace: defender keeps title
- Surrender: defender keeps title; attacker pays gold

Ritsuryō Imperial Policy Defense Mobilization: vassals unlock Imperial Reconquest of Japan CB (all de jure Empire of Japan counties).

## Subjugate Wars

Available to independent neighbors. Requirements (any one):
- Tribal/Wanua gov + Distinguished fame + target has Tribal/Wanua gov
- Eastern religion + Exalted Among Men fame + target has Eastern religion
- Temporal Head of Faith + Devoted Servant devotion + same faith target (costs additional 1000 Piety)
- Demand Local Submission decision

Prestige costs:

| Rank | Non-Tribal/Wanua | Tribal/Wanua |
|------|------------------|-------------|
| County | 1000 | 500 |
| Duchy | 1000 | 500 |
| Kingdom | 1500 | 750 |
| Empire | 2500 | 1250 |

Outcomes:
- Enforcing demands: attacker becomes liege; if defender's rank higher, attacker takes it
- White peace: defender remains independent
- Surrender: defender remains independent; attacker gains +25 faction discontent

### Forced Vassalization

Targets rulers with realm of 3+ counties (plus 2 per innovation: Casus Belli, Chronicle Writing, Divine Right, Rightful Ownership). Cannot target Heads of Faith. Requires (any one): Forced Vassalization perk, Conqueror trait, Iberian Struggle Hostility phase involvement.

## Holy Wars

Target rulers with Hostile or Evil faith; require organized faith without Pacifism/Dharmic Pacifism tenets. Cost is Piety.

Outcomes:
- Enforcing demands: attacker gains all Hostile/Evil faith titles; vassalizes others in war target; defender gains double attacker's fervor cost
- White peace: defender keeps titles; attacker loses 50 Piety
- Surrender: defender keeps titles; attacker pays gold, gains +25 faction discontent, -15 vassal opinion (5 years)

Holy War costs by target:

| Target | Devotion | Fervor | Base Cost | Armed Pilgrimages Cost | Contribution | Once/Lifetime |
|--------|----------|--------|-----------|----------------------|--------------|---------------|
| County | Dutiful | 1 | 100 | 80 | 100 | No |
| Duchy | Faithful | 2 | 200 | 160 | 200 | No |
| Kingdom | Paragon of Virtue | 5 | 750 | 600 | 500 | Yes |

## Artifact Wars

Against characters owning artifacts with claims or holy relics, different faith. Cost 150 Prestige.

Outcomes:
- Enforcing demands: attacker gains all valid artifacts; defender gains claims on lost artifacts
- White peace: defender keeps artifacts
- Surrender: defender keeps artifacts; attacker loses all claims and pays gold

## Bring Under Tribute

Independent rulers vs. neighbors of equal/lower rank. Nomadic rulers ignore authority law requirement. Cost 25-300 Prestige (Mandala = Piety) based on target realm size.

Outcomes:
- Enforcing demands: defender becomes tributary with max obligations
- White peace: defender remains independent
- Surrender: defender remains independent; attacker gains +25 faction discontent

### Retaliation War

Available to suzerains if nomad/adventurer nomad migrates to tributary lands and refuses vassalization. Defender pays scaled Herd on attacker victory.

## Eradicate Rival House

Between feuding houses (not liege/vassal). Cost 85 Prestige. Winner gains 750 Prestige and all loser's titles.

If loser is AI: winner gains 20 Dread, house gains Rival House Eradicated modifier. Loser and spouse (except heir) are killed; heir and outside family get -50 opinion. Heir joins highest-opinion Count+ vassal's court or becomes adventurer/landless.

If loser is player: house gains House Eradicated modifier; player can attempt Intrigue challenge. Success saves everyone but keeps modifier. Heir follows same court/adventurer rules.

## Excommunication War

Against excommunicated rulers of same faith.

Outcomes:
- Enforcing demands: defender deposed; attacker gains 20 opinion with Head of Faith
- White peace: defender keeps titles; attacker loses 50 Piety
- Surrender: defender gains 150 Piety and loses Excommunicated trait; attacker loses 50 Piety and 20 opinion

## Raid for Captives

Human Sacrifice faith tenet required. Cost 100 Piety (80 with Armed Pilgrimages), half cost with Tribal gov.

Outcomes:
- Enforcing demands: attacker imprisons 3-5 defender courtiers
- White peace: no prisoners
- Surrender: no prisoners; if defender has Human Sacrifice, defender imprisons 3-5 attacker courtiers

## Rescue House Members

House heads with Bound by Blood perk (75 Prestige cost) or Clan gov with Friendly/Harmonious unity (prestige scales). Targets rulers imprisoning house members.

Outcomes:
- Enforcing demands: attacker releases imprisoned house members; Clan gov gains 4 unity per freed (max 20)
- White peace: members remain imprisoned
- Surrender: members remain imprisoned; attacker loses 350 Prestige

Note: If captured members are heirs, war score shifts toward defender.

## Unify The House

House heads with Bound by Blood perk (150 Prestige per targeted member) or Clan gov Friendly/Harmonious unity (scales). Targets rulers with Duke+ house vassals.

Outcomes:
- Enforcing demands: defender's house vassals become attacker's; Clan gov gains 4 unity
- White peace: members remain defender's vassals
- Surrender: members remain defender's vassals; attacker loses 350 Prestige; Clan gov loses 4 unity

## Migrate to Pannonia

Táltosist faith only, declared once per game with Prepare to Cross Carpathians decision. Targets Pannonian Basin. If Hungarian Migration rule is Immediate, game starts with Mogyër Confederation vs. Bulgaria.

Success effects:
- Attacker gains all defender's Pannonian Basin titles
- Attacker gains Kingdom of Hungary (replaces Kingdom of Pannonia)
- Other kingdom titles destroyed
- Titles outside de jure Hungary given to new characters of their culture/religion
- Non-de jure Hungary vassals become independent
- Controlled counties convert to Mogyër culture/Táltosist faith
- Previously controlled counties convert to Pecheneg culture

War spawns attacker army:

| Years | Levies | Horse Archers |
|-------|--------|---------------|
| 867-889 | 3000 | 2000 |
| 890-904 | 5000 | 3000 |
| 905+ | 6000 | 4000 |

## Raid Wars

Neighbors only. Available if:
- Both in Iberian Struggle (Opportunity/Hostility phase): 75 Prestige (50 additional Piety if same faith)
- Vassal with Admin gov after peace threshold: 30 Influence

Always targets border county.

Outcomes:
- Enforcing demands: attacker gains 5 gold per development, 25 per building; war target loses 1 development, 25 control, -50% taxes/construction, -10% development (5 years), 25% chance random building destroyed
- White peace: unaffected
- Surrender: unaffected; attacker pays defender gold

## Varangian Adventure

Tribal Era only, non-kings, no concurrent wars. Requires Varangian Adventurers innovation, Prestige cost increases per use. Targets counties/duchies of different culture group.

Success effects:
- Attacker's titles destroyed/redistributed
- Vassals gain independence
- Attacker gains target title and de jure parts
- Attacker gains Adventurer trait and 200 gold
- County target: duchy given if unexisting/defender-held
- Feudal target: government changes to Feudal

War spawns attacker army based on Mainland Scandinavia counties of same faith/culture:

| Counties | Varangian Veterans | Bondi | Vigmen | Huscarls |
|----------|-------------------|-------|--------|----------|
| 1 | 100 | 0 | 0 | 0 |
| 2 | 300 | 0 | 0 | 0 |
| 3 | 300 | 200 | 0 | 0 |
| 4 | 300 | 400 | 0 | 0 |
| 5 | 300 | 400 | 200 | 0 |
| 6 | 300 | 400 | 400 | 0 |
| 7 | 300 | 400 | 600 | 0 |
| 8 | 300 | 400 | 800 | 0 |
| 9 | 300 | 400 | 800 | 200 |
| 10 | 300 | 400 | 800 | 400 |

Plus 100 levies base (200 with Adventure legacy 1). Adventure legacy 1 also adds 400 Varangian Veterans, 100 Bondi, 400 Vigmen.

AI uses only if all titles in Mainland Scandinavia; requires Ambitious + two of (Adventurer, Arrogant, Brave, Greedy) unless Scandinavian Adventurers rule is Apocalyptic.

## Install Loyalist

Iranian Intermezzo Unrest phase only. Requires Supporter of Caliphal Authority trait, targets Detractor of Caliphate with Count+ Supporter vassal. Cost 250 Piety.

Outcomes:
- Enforcing demands: Supporter vassal takes defender's primary title; attacker gains 100 Piety, 65 opinion (30 years), alliance, and Strong Hook if attacker is caliph/Abbasid emperor
- White peace: defender keeps title
- Surrender: defender keeps title; attacker loses -20% Fame Impact and -10 Vassal Opinion (10 years)

## Humiliation War

Nomadic government only. Targets characters with higher Dominance law (not highest level). Cost 75 Prestige.

Outcomes:
- Enforcing demands: defender's Dominance reduced one level; border counties given to Herders; defender pays Herd (Disobedient 5 years)
- White peace: nothing
- Surrender: attacker pays defender gold

## Raze Capital Temple Complex

Mandala government only. Cost 100 Piety.

Outcomes:
- Enforcing demands: defender's capital temple complex ruined (requires repair)
- White peace: nothing
- Surrender: attacker's capital temple complex ruined (requires repair)

## Plunder for Contribution

Mandala house heads with Destruction aspect who started great project. Targets Mandala rulers. Cost 100 Piety.

Outcomes:
- Enforcing demands: defender forced to contribute to attacker's great project
- White peace/Surrender: nothing

## Enforce Administrative Integration

Ritsuryō vassals vs. Sōryō vassals. Cost 180 Prestige.

Outcomes:
- Enforcing demands: attacker gains 120 Influence and 25 opinion with liege; liege takes loser's titles
- White peace/Surrender: nothing

## Consolidate Land Under Heaven

Dynastic Cycle Tension era only. Targets neighbor rulers with Hegemony of China territory. Cost 100 Piety (same faith) or 150 Prestige (different).

Outcomes:
- Enforcing demands: attacker takes defender's equal+ titles; vassalizes defenders with capitals in Hegemony of China de jure
- White peace: nothing
- Surrender: attacker pays gold and loses 350 Prestige

## Decision Wars

Cannot be declared normally; must use decision. No white peace option.

- **Holy Roman-Byzantine Imperial War**: Dismantle Greek/German Pretenders decisions. Surrender = massive gold payment. Success = defender's primary title destroyed, land becomes attacker's de jure.
- **[Khans of the Steppe] Domination Wars**: Dominate Title decision. Success = attacker gains title, all defenders become Obedient tributaries.
- **[Khans of the Steppe] Great War of Defiance**: Become Greatest of All Khans decision. Surrender = 90% Herd/Gold/Prestige loss, 500 Legitimacy, -1 fame, Dreams modifier loss, domain to Herders, subjects independent, Dominance to Limited, imprisonment. Success = Greatest of Khans trait, 1500 Prestige, 500 Legitimacy, +1 fame, Mongol Empire title, The Golden Lineage modifier, all defenders vassals (Obedient 10 years), all truces ended, nicknames offered, 19200 Horde Riders + other units/war gear.
- **War to Establish Sōryō Administration**: Establish Sōryō Administration decision. Surrender = strongest defender takes Empire of Japan and attacker's vassals. Success = attacker/bloc members change to Sōryō, defenders imprisoned.

## Related Topics

See [Warfare Overview](warfare-overview.md), [Army](army.md), [Hired Forces](hired-forces.md), [Knights](knights.md).
