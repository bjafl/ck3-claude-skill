---
title: Alliance
category: intrigue-and-diplomacy
tags: [alliance, war, diplomacy, confederation]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Alliance]
---

Alliances permit two characters to call upon each other in wars, prevent faction membership against each other, and block title revocation unless the vassal commits a crime. Declaring war on an ally incurs -25 popular opinion for 3 years. Alliances end automatically if requirements cease, though ongoing wars continue. Only Counts and above can form alliances.

## Creating an alliance

Alliances form automatically between married characters or when close family members of two rulers marry or become betrothed. Marriage proposals show whether they create alliances. Rulers at peace and not imprisoned may negotiate alliances under these conditions:

- Characters are close or extended family (not cousins).
- Proposer has Defensive Negotiations perk (not available vassal-to-liege).
- Both are house heads with faithful house relation.
- Either has parents or spouses who are blood siblings.

In multiplayer, rejected alliance offers cannot be reissued with the same character. Hegemons cannot negotiate alliances but form marriage alliances.

### Acceptance calculation

Acceptance ranges:

- Military strength difference: -1000 to +100
- Title rank difference: -120 to +120
- Opinion: -100 to +25
- Legitimacy: -100 to +50
- Friends: +25
- Lovers: +25
- Liege relationship: +20
- Close family: +20
- Same house: +10
- Extended family: +10
- Primary heir: +10
- War within last 12 years: -100
- Rivals: -100
- Nemeses: -300

Hooks can increase acceptance. Rulers with influence-based government can spend influence.

Blood siblings automatically have an alliance with each other.

## Joining wars

Allies have two ways to participate: the targeted character can accept an offer to join, or the war leader can call them. Acceptance depends on opinion and honor, modified by:

| Source | Acceptance |
|---|---|
| Heir | always |
| Spouse | always |
| Defensive war | +50 |
| Defensive war against their ally | -25 |
| Offensive war against their ally | -50 |
| Holy war against same faith | -50 |
| Enemy is friend | -50 |
| Enemy is best friend | -100 |
| Enemy is lover | -100 |
| Enemy is soulmate | -100 |
| Enemy is heir | never |
| Enemy is spouse | never |
| Conqueror | never |

### War costs and penalties

Defensive wars cost nothing. Offensive wars cost prestige by ally title rank:

| Title rank | Cost |
|---|---|
| Count | 75 |
| Duke | 150 |
| King | 350 |
| Emperor | 750 |
| Hegemon | Free (emperors/hegemons only) |

Allies declining offensive wars lose -20 opinion for 5 years and 350 fame. Declining defensive wars lose -50 opinion for 25 years and 750 fame.

### War contribution

Wars lasting 2+ years with an ally at 0% contribution trigger demands. The ally must pay gold/prestige or promise to earn contribution within a year. Breaking the promise costs a fame level and -50 opinion with the war leader.

## Confederations

Confederations are alliances of independent Counts or Dukes who join defensive wars automatically but not offensive ones. Members cannot attack each other, raid each other, create titles, or exceed authority law level 2. Confederation realms display the founder's map color.

Only tribal or nomadic rulers can create or join. Nomadic members gain -25% fertility consumption for 5 years and +30 fertility in their nomadic capital county. The modifier disappears if leaving. Members automatically leave if they migrate.

Creating a confederation requires the Call for Confederation decision, unlocking the offer interaction. Acceptance increases with prestige/herd spending or hooks; decreases above 3 members.

Same-culture confederations are named after the culture; others after the founder's de jure duchy.

### Elevating confederations

Once 5+ members exist, the member with highest fame level can unify the confederation into a single kingdom. Requires 25+ opinion with all members and costs 150 prestige. Unification effects:

- Character gains a kingdom with confederation elective succession law (no de jure lands until duchy assimilation).
- Other members become vassals.
- Character gains First King of the Confederation modifier 15 years: +1 monthly prestige, +10 defender advantage, +20% legitimacy gain, -50% men-at-arms recruitment, +20 vassal opinion, +20% herd gain, +50% title creation cost.
- All confederation member counties gain Confederate Lands modifier 30 years: +5 defender advantage, +0.3 monthly control, +20% fertility growth.
- All vassals gain permanent Vassal of the First King modifier.
