---
title: Clan government
category: realm-and-succession
tags: [government, clan, tax jurisdiction, tax collector, house unity, vizier]
game_version: "1.19"
dlc: []
sources:
  - https://ck3.paradoxwikis.com/Clan_Government
---

Clan is predominant in Muslim North Africa, the Middle East, and Persia. Clan rulers can create new holdings and cadet branches, and use the Crown Authority law (see [Feudal](government-feudal.md) § Crown Authority). Powerful vassals want an alliance with their liege and get −30 opinion if they lack one. At peace, clan rulers can appoint a Vizier. House heads can grant/remove the Extolled by House or Accused of Decadence traits on house members. If a clan ruler is a Dynasty Head, their realm is named after their dynasty rather than their primary title (can be disabled in settings).

## Tax Jurisdictions

Clan vassals pay taxes/levies through Tax Jurisdictions, visible on the sidebar once a ruler has any Clan vassals. Each jurisdiction has one Tax Collector and up to 12 Taxpayers (auto-assigned, manually adjustable). Count/Duke rulers can appoint 1 Tax Collector, King/Emperor/Hegemon rulers 2; +1 more for the Enlightened Magnates or Legalistic culture tradition, the 1st Brilliance dynasty legacy, Magistrates/Court Officials innovations, or the Avaricious lifestyle's Golden Obligation perk (1 each). A Vizier grants 1–5 more depending on Stewardship. Courtiers and clan vassals can be appointed Tax Collector if the faith's View on Gender doctrine allows it.

Tax Collector aptitude: +1 per Diplomacy/Martial/Stewardship/Intrigue skill (max 50 each), +2 per Learning (max 50), +5 per 20 opinion, +10 each for Just/Administrator/Avaricious/Diplomat trait, +15 for Enlightened Magnates tradition, +20 for Family Business tradition, −10 if a vassal.

| Aptitude | Gold contribution | Levies contribution |
|---|---|---|
| Terrible (0-19) | 0% | 0% |
| Poor (20-44) | 2% | 4% |
| Average (45-74) | 6% | 12% |
| Good (75-109) | 12% | 24% |
| Excellent (110+) | 20% | 40% |

### Tax Decree

Set per jurisdiction, changeable once every 5 years; vassals who no longer qualify are dropped as taxpayers.

| Decree | Taxes | Levies | Liege effect | Vassal effect | Requirement |
|---|---|---|---|---|---|
| Basic Taxes | +20% | +20% | — | — | — |
| Zakat | +40% | +20% | +1% domain taxes | +10% monthly piety, −30 opinion of liege | — |
| Iqta Grant | Normal | +10% | +1% MaA damage | −10% MaA recruit/maintenance cost, +15 opinion of liege | — |
| Ghazi Status | +10% | Normal | +2% monthly piety, +1 zealot vassal opinion | Can raid; +10% income at war; +0.5 monthly piety; +15% raid speed; +15% siege weapon effectiveness; +0.25 monthly control growth; −50% holy war CB cost; +25% other CB cost | Taxpayers must share the liege's faith |
| Jizya Status | +100% | −75% | −0.2 monthly prestige | Liege can't demand conversion/revoke title/convert vassal's faith; different faith isn't a revocation reason | Tax Nonbelievers tenet or Jizya doctrine; taxpayers must be a different religion |
| Muqata Status | Normal | Normal | +0.1 monthly prestige | +10% development growth, +10 plague resistance, +15 popular opinion, +30 opinion of liege, −5 danger | Legacy of Persia DLC |
| Dehqan | +35% | +35% | +1% legitimacy gain | +20% monthly prestige | Legacy of Persia; Enlightened Magnates tradition |
| Maguh Status | Normal | Normal | +1% development growth | −10% holding/building construction cost, +0.1 monthly development in realm capital, +30 opinion of liege | 4th-level Brilliance dynasty legacy |

## House Unity

If a house head has Clan government, the house gets a House Unity stat (0–200, 5 levels), raised by Unifying Actions (e.g. Extol Virtuousness, gift artifact, negotiate alliance, restore inheritance) and lowered by Divisive Actions (e.g. blackmail, declare war, revoke title, expose a secret). House heads can use the Steer House Unity decision. All house members using multiple-heir succession share the same succession law.

| Level | Range | Border wars | Invasion CB | CB cost | Claimant faction accept. | Lifestyle XP | Dread decay |
|---|---|---|---|---|---|---|---|
| Antagonistic | 0-39 | Conditional Join | Unlimited | −30% | +40 | — | — |
| Competitive | 40-79 | Guaranteed Protection | Every 10y | −15% | +20 | +5% | — |
| Impassive | 80-119 | Guaranteed Protection | Once/lifetime | — | — | +10% | — |
| Friendly | 120-159 | Guaranteed Protection | No | +15% | −20 | +5% | −20% |
| Harmonious | 160-200 | Guaranteed Protection | No | +30% | −40 | — | −40% |

Friendly/Harmonious unlock Rescue House Members and Unify the House casus belli for the House Head. Each House Unity decision usable once per 20 years, e.g. Reinforce Army with Loyal Officers (Antagonistic; scaled gold + 200 piety + 20/landed member; Loyal Army Officers modifier 10y), Enforce Intrigue Network (Competitive; 200 piety; Intrigue Network modifier 10y), Consult House Members (Impassive; 100 piety; +10% councilor task progress), Send Bailiffs (Friendly; scaled gold+200 piety; Enforced Bailiffs 10y), Placate Vassals (Harmonious; scaled gold+200 piety; Placated modifier 10y). Culture/DLC-gated variants also exist (Futuwaa Lodges, Madrasas, Shared Army Logistics, Promote Development — Legacy of Persia + Iranian heritage or specific traditions required).

Most houses start at 100 Unity (Impassive) in 867, except: House Abbasid (Antagonistic), House Samanid (Competitive), House Afrighid (Friendly), House Tahirid and House Umayyad (Harmonious). Custom characters replacing these houses inherit their starting Unity.

## Converting to Clan

Tribal vassals and independent rulers can adopt Clan ways via decision.
