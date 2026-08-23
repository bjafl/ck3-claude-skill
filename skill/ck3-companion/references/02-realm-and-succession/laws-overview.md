---
title: Laws Overview
category: realm-and-succession
tags: [laws, authority, policies]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Laws]
---

Laws are royal decrees with vital effects on realm development. Decreasing law levels is free and unrestricted; increasing costs Prestige.

## Border Wars Policy

Automatically set law dictating liege participation in vassal defensive wars against foreign rulers (cannot be manually changed).

**Conditional Join**: Active when title rank is Hegemony, realm size 160+, active civil war, or Antagonistic House Unity. Liege doesn't automatically join vassal defensive wars but can use Protect Vassal interaction after 3 years. Certain factions gain Discontent twice faster.

**Guaranteed Protection**: Active when title rank isn't Hegemony, realm size <160, no civil war, and House Unity isn't Antagonistic. Liege automatically joins vassal defensive wars.

## Administrative Laws

Administrative governments access the following laws (200 Prestige cost, increased by 1 per Realm Size, reduced by 1 per Learning).

**Provincial War Declaration**: Dictates which governors wage external wars (requires Imperial Bureaucracy law at same/higher level):
- Level 1: All governors can declare
- Level 2: Only Frontier/Naval governors
- Level 3: Only Frontier/Naval governors (require permission)
- Level 4: No governors can declare

**Provincial Border Policy**: Dictates which governors use Boundary Dispute/Subsume Governorship schemes (requires Imperial Bureaucracy 1+ level above):
- Level 1: Governors can use
- Level 2: Only Powerful/Dominant Family governors can use; -5 administrative vassal Opinion
- Level 3: No governors can use; -10 administrative vassal Opinion

## Celestial Laws

Independent Celestial government rulers access the following laws (200 Prestige cost, increased by 1 per Realm Size, reduced by 1 per Learning).

**Retirement Age**: Sets governor retirement age (50/60/70/80/90). Above-retirement governors have reduced candidate scores, unlock Retire from Heading the House decision, and liege can use Retire Governor interaction.

**Army Command Structure**: Decides how military governors own men-at-arms:

| Law | Men-at-arms | Title Men-at-arms | Call Cost | Vassal Effect | Requirements |
|---|---|---|---|---|---|
| Autonomous Command | +2 |  | Regular | -5% Tax Contribution |  |
| Regional Command | -2 | +1 | -25% | -5 Opinion | Can afford |
| Imperial Command | No |  | -50% | -10 Opinion | Can afford |
| Grand Expansionist Command | No | +2 | -75% | -15 Opinion | Expansion phase |

### Hegemony of China Laws

Two additional laws available while government remains Celestial:

**General Secretariat Control**: Dictates which councilor is Grand Secretariat diarch (Grand Chancellor/Grand Marshal/Imperial Censor). No cost to change; only during Advancement phase or when Advancement is favored movement. AI always keeps Grand Chancellor unless human player is other option.

**Candidate Score Focus**: Determines if fame/splendor levels affect candidate scores (only same-government characters). Costs 1000 Influence and scaled Treasury. Starts Merit; changing to Family requires Conservative Movement as favored and 5 Ministries + 3 Powerful Family heads.

## Imperial Policy

Independent emperors with Ritsuryō/Sōryō government access Imperial Policy law (500 Prestige to change). Vassals can change via Imperial Policy faction ultimatum acceptance or civil war victory.

| Law | Effects | Vassal Opinion | Description |
|---|---|---|---|
| Disarmament | +15% Development +25% Men-at-Arms Maintenance +50% Internal Casus Belli Cost Can construct/upgrade castles | -15 Sōryō | Peace requires seized weapons |
| Enforced Isolation | +15 Plague Resistance +25% Physician Aptitude -15% Development -15% Diplomatic Range Reduced plague spread | None | Outsiders threaten stability |
| Imperial Pacification | -15% Men-at-Arms/Mercenary costs -25% Armory/Stable cost +20 Danger Unlocks Imperial County Pacification casus belli | -35 Ritsuryō | Safeguard borders |
| Manor Reform | -15% Building time/cost +25% Domicile building time/cost -25% Domicile Influence | -15 Ritsuryō | Redistribute land prevent corruption |
| Banditry Crackdown | +0.2 Monthly Control +5% Control Growth -10% City cost -10 Danger -15% Development | +15 Minor Landholder | Restore countryside order |
| Defense Mobilization | +1 Fort +15% Hostile Raid Time -25% Armory/Stable cost -15% Men-at-Arms Maintenance +5 Advantage same culture Unlocks Imperial Reconquest casus belli | None | Unite against threats |

Only passable during defensive war or when not owning all Japan de jure counties.

## Coronation

Every King+ has Coronation law (if Coronation Laws game rule enabled). Cannot be manually changed; automatically increases upon completing Coronation activity. New rulers start lowest level. Ceremonial Monarchy realms don't have Coronation law unless both monarchs are same character. Ritsuryō/Sōryō rulers only have if top liege.

| Level | Effects | Source |
|---|---|---|
| Uncrowned | -2.5 Monthly Legitimacy -25% Legitimacy Gain -10 Vassal Opinion Character/spouse cannot use Crown/Regalia artifacts | New ruler |
| Crowned Sovereign | +5 Courtly/Minor Landholder Opinion Character/spouse can use artifacts | Coronation activity |
| Anointed Sovereign | +10 Courtly/Minor Landholder/Zealot Opinion Character/spouse can use artifacts | Anointment activity |
