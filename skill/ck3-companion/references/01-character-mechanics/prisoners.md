---
title: Prisoners
category: character-mechanics
tags: [imprisonment, ransom, torture, execution, punishment, crimes]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Prisoner]
---

Prisoners are characters held involuntarily at your court, acquired through the Abduction scheme, occupying enemy realm capitals during war, or defeating enemy commanders in battle. You can imprison any character within your realm, but this incurs tyranny unless the prisoner is guilty of a crime or is not of noble rank. Imprisoned characters can be released, ransomed, tortured, executed, or subjected to various punishments depending on your culture and faith.

## Obtaining and Mechanics

Prisoners in the third or closer line of succession to a ruler's primary title provide war score against that ruler but are automatically released when any war ends.

### Prisoner Value

A prisoner's worth depends on their title rank when released, ransomed, or punished:

| Title rank | Ruler/Primary Heir | Spouse | Close Family | Other | Execution/Torture Dread | Castrate/Blind Dread | Legitimacy from Release | Execution Artifact |
|---|---|---|---|---|---|---|---|---|
| Unlanded | — | — | — | 10 | 0 | 10 | 0 | None |
| Baron | 30 | 15 | 10 | 10 | 0 | 10 | 0 | None |
| Count | 50 | 25 | 15 | 10 | 5 | 20 | 0 | Can only send to heir |
| Duke | 100 | 50 | 25 | 10 | 10 | 20 | 20 | Can only send to heir |
| King | 200 | 100 | 50 | 20 | 15 | 30 | 40 | Famed |
| Emperor | 500 | 250 | 125 | 50 | 30 | 30 | 60 | Illustrious |
| Hegemon | 1000 | 500 | 250 | 100 | 60 | 60 | 120 | Illustrious |

### Imprisonment Effects

Prisoners are held in either the dungeon or house arrest, which can be changed freely. By default, lowborn prisoners go to the dungeon while nobles are placed under house arrest. Both locations impose significant penalties:

|  | House Arrest | Dungeon |
|---|---|---|
| Diplomacy | -5 | -5 |
| Natural Dread | -20 | -30 |
| Dread Loss | -100% | -100% |
| Monthly Lifestyle Experience | -75% | -150% |
| Stress Gain | 0% | +50% |
| Prisoner Family Opinion | 0 | -15 |
| Health Penalty | None | Severe |
| Illness Risk | None | After 5 years |
| Escape Chance | Normal | Reduced |

Prisoners accumulate stress over time and will eventually die if stress becomes too high.

## Negotiate Release

You can offer to release a prisoner in exchange for conditions or demands:

| Condition | Acceptance | Opinion Bonus (10 years) | Requirements |
|---|---|---|---|
| Gain Weak Hook | -80 | -20 | — |
| Demand Conversion | -20 | -10 | Different faith; prisoner is vassal/non-ruler; prisoner is not head of faith |
| Banish | -50 | -20 | Prisoner is not independent ruler; not an adventurer |
| Recruit | -10 | -15 | Prisoner is not ruler/adventurer/courtier |
| Renounce Claims | -25 | -30 | Prisoner has claims on your titles |
| Take the Vows | -30 | -10 | Same faith; faith has Monasticism tenet; prisoner is family/courtier |

Releasing with no demands costs 10 Dread and gives 20 Opinion for 10 years. High-ranking prisoners released without demands may grant Legitimacy.

## Ransom

Ransoming allows you to exchange gold or a weak hook for a prisoner's freedom. The ransom recipient is determined in order:

1. The prisoner themselves (if landed)
2. Their direct liege (if courtier)
3. The prisoner themselves (if unlanded)

Prisoners and their liege may offer ransom, or use a hook on you. When a liege pays ransom for a vassal or courtier, that character gains +5 opinion for 1 year.

Ransom cost depends on the recipient's primary title rank and their relation to the prisoner. If you have the Golden Obligations perk, ransom costs increase to approximately 6 times your tax income (minimum 50, maximum 300 gold). Unlanded, liegeless characters cost 100 gold with the perk or if they have 100+ gold spare.

## Punishment

### Execution

Executing a prisoner incurs -20 Opinion with their dynasty, -25 with their liege, -30 with friends/lovers, -50 with family/spouses, and +2 Tyranny (unless they are guilty of severe crimes or follow a Hostile/Evil faith).

Three execution methods are available:

| Method | Piety | Requirements |
|---|---|---|
| Behead | -25 lowborn / -100 noble | Same faith [Yes] or faith lacks Gruesome Festivals tenet [No] |
| Burn at Stake | +25 if Fundamentalist doctrine | Same faith [No] and faith lacks Gruesome Festivals tenet [No] |
| Sacrifice | +50 same faith / +250 different faith | Faith has Gruesome Festivals tenet [Yes] |

You can enhance executions with additional options:

- **Devour**: Characters with the Cannibal trait or faiths with Ritual Cannibalism can devour the prisoner (−35 Stress, 20% chance to gain Ill trait, gain Cannibal trait).
- **Public Execution**: Executioners can make executions public (+15 Popular Opinion in realm capital for 5 years, +3 Control per Aptitude level).
- **Long Pig**: Adventurers with the Long Pig perk can convert the prisoner to Provisions.

If you have a royal court and possess the Arbitrary, Deceitful, Callous, Sadistic, or Vengeful trait, executing a rival has a 25% chance to turn their skull into a pedestal artifact (guaranteed if they were your nemesis). Lacking an Executioner causes −30 Opinion with your Personal Physician or Antiquarian.

### Torture

Torturing grants:

- −100 Piety (unless faith has Exaltation of Pain or you have Divine Retribution perk)
- +100 Piety if faith has Exaltation of Pain tenet
- −10 Stress if you have the Sadistic trait
- +10 Stress if you have the Trusting trait
- +100 Stress if you have the Compassionate trait

The tortured character loses −75 Opinion for 50 years toward you and gains the Recently Tortured modifier (−0.75 Health for 5 years). They can reveal secrets to avoid torture.

### Tradition-Based Punishments

Available only to adult characters if your culture has certain traditions:

**Castration** (requires Amharic Highlanders, Court Eunuchs, Byzantine Traditions, or Palace Politics): Characters under 12 gain Beardless Eunuch; others gain Eunuch. 66% chance of major Health/Stress penalty for 5 years (reduced to 50-15% with Personal Physician depending on Aptitude). Causes −50 Opinion for 50 years with prisoner and −20 Opinion for 20 years with their close family/spouses.

**Blinding** (requires Byzantine Traditions, Merciful Blindings, or Palace Politics): Prisoner gains Blind trait. Causes −50 Opinion for 50 years and −20 Opinion for 20 years with close family/spouses.

**Maiming** (Duumvirate only): Ends power sharing. Choose to give Blind, Disfigured, One-Legged, or Maimed (males also can be castrated). Co-emperor takes all titles except the family nobility one.

### Sun Trial

Available to faiths with Sun Worship tenet, only against criminals. You gain 100 Piety. Prisoner either dies or survives; if they survive with the same faith, they gain +3 Monthly Piety and +15 Same Faith Opinion for 15 years. Survival chance depends on realm capital terrain and prisoner's health.

## Crimes

Crimes allow you to imprison someone without incurring tyranny and may remove tyranny from punishments. Crimes can be pardoned for opinion bonuses.

### Standard Crimes

| Crime | Duration | Title Revocation | Banishment | Execution |
|---|---|---|---|---|
| Declared War | 12 years | Yes | — | — |
| Tortured Me | 50 years | — | — | — |
| Blinded Me | 50 years | — | — | — |
| Castrated Me | 50 years | — | — | — |
| Refused Revocation of Title | 20 years | Yes | — | — |
| Refused Imprisonment | 20 years | Yes | — | — |
| Refused Retraction | 20 years | Yes | — | — |
| Attempted Arrest | 15 years | — | — | — |
| Embezzled From Me | 10 years | Yes | — | — |
| Orchestrated Coup | 50 years | Yes | — | — |
| Usurped my Regent | 20 years | Yes | — | — |
| Plotting against Me | 10 years | — | — | — |
| Stole Artifact from Me | 15 years | — | — | — |
| Tried to Steal Artifact | 5 years | — | Yes | Yes |
| Attempted To Murder Me | Permanent | — | Yes | Yes |
| Attempted Abduction | 10 years | — | Yes | — |
| Abducted Me | Permanent | — | Yes | — |
| Elopement | 30 years | — | — | — |
| Attempted Elopement | 15 years | — | — | — |
| Scheming Against Me | 10 years | — | — | — |
| Spying on Liege | 10 years | — | — | — |
| Escaped Prison | 10 years | — | — | — |
| Revolted against Me | 15 years | Yes | — | — |
| Botched My Treatment | 10 years | — | Yes | Yes |
| Failed To Treat Me | 10 years | — | — | — |
| Slept With My Spouse | 15 years | — | — | — |
| Burned My Orchard | 10 years | — | — | — |
| Plotting Against Liege | 20 years | — | — | — |
| Traitor | 20 years | — | — | — |
| Hurt Someone Close to Me | Permanent | — | — | — |
| Murdered Someone Close to Me | Permanent | — | — | — |
| Theft | 20 years | — | — | Yes |
| Attempted to Seize my Realm (requires Roads to Power) | Permanent | — | — | — |
| Seized my Realm (requires Roads to Power) | Permanent | — | — | — |
| Attempted to Raid my Estate (requires Roads to Power) | Permanent | Yes | Yes | Yes |
| Raided my Estate (requires Roads to Power) | Permanent | Yes | Yes | Yes |
| Stole my Herd (requires Khans of the Steppe) | 15 years | — | — | — |
| Stole my Liege's Herd (requires Khans of the Steppe) | 5 years | — | — | — |
| Stole my Vassal's Herd (requires Khans of the Steppe) | 5 years | — | — | — |
| Attempted to Steal my Herd (requires Khans of the Steppe) | 5 years | — | — | — |
| Tried to Become the Greatest of Khans (requires Khans of the Steppe) | 10 years | Yes | Yes | Yes |
| Abused Authority (requires Khans of the Steppe) | Permanent | Yes | Yes | Yes |
| Established Fief | 40 years | Yes | Yes | — |

### Familial Crimes

Any ruler who is a close family member of the victim can imprison the criminal:

| Crime | Duration | Banishment | Execution |
|---|---|---|---|
| Botched Treatment of Kin | 10 years | Yes | Yes |
| Failed To Treat Kin | 10 years | — | — |
| Tortured Family Member | 20 years | — | — |
| Attempted To Murder Family Member | Permanent | Yes | Yes |
| Murdered Family Member | Permanent | Yes | Yes |
| Abducted Family | Permanent | Yes | Yes |
| Unlawfully Executed Family | Permanent | Yes | Yes |
| Attempted to Seize Close Family's Realm (requires Roads to Power) | Permanent | — | — |
| Seized Close Family's Realm (requires Roads to Power) | Permanent | — | — |

### Religious Crimes

Characters with infamy traits that their faith considers crimes are viewed as criminals by all believers of that faith:

| Trait | Conditions | Title Revocation | Banishment | Execution |
|---|---|---|---|---|
| Cannibal | Faith lacks Ritual Cannibalism tenet | — | — | Yes |
| Excommunicated | Faith has Communion tenet | Yes | Yes | — |
| Adulterer | Faith has criminal adultery doctrine for gender | Yes | — | — |
| Fornicator | Faith has criminal adultery doctrine for gender | Yes | — | — |
| Deviant | Faith has criminal deviancy doctrine | Yes | — | — |
| Sodomite | Faith has criminal same-sex relations doctrine | Yes | — | — |
| Witch | Faith has criminal witchcraft doctrine | — | — | Yes |
| Dynastic Kinslayer | Faith has dynastic kinslaying doctrine | — | Yes | Yes |
| Familial Kinslayer | Faith has dynastic or familial kinslaying doctrine | — | Yes | Yes |
| Kinslayer | Faith has any kinslaying doctrine | — | Yes | Yes |
