---
title: Succession
category: realm-and-succession
tags: [succession, inheritance, heirs]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Succession]
---

Succession handles the inheritance of titles, gold, men-at-arms, and artifacts upon ruler death or abdication. The player heir is the character the player continues as upon succession (always primary heir unless they belong to a different dynasty).

## Eligibility

Character eligibility for inheritance is determined by laws, doctrines, and traits. Some traits disinherit their owner and descendants (disinherited characters don't inherit claims either):

- Gender law determines male-only, female-only, or both inheritance (preference laws make the other gender ineligible only if eligible opposite gender exists)
- Theocratic rulers cannot inherit
- Disqualifying traits: Bastard, Bastard Founder, Child of Concubine (if monogamous/polygamous liege), Disinherited (if same dynasty), Eunuch, Monk/Nun (doesn't disinherit descendants, still inherits claims), Order Member (doesn't disinherit descendants, still inherits claims)

## Realm Succession

The realm succession law applies to all titles without individual succession law assignments.

### Single Heir Laws

**Primogeniture**: Oldest child inherits all titles. If dead, seeks living heir among their descendants. If none, goes to oldest sibling, then their descendants, then lateral branches, then primary parent (father patrilineal/mother matrilineal), then their siblings.

**Ultimogeniture**: Youngest child inherits all titles, following same descent rules as Primogeniture.

**House Seniority**: Oldest house member inherits. With male/female preference, opposite gender only inherits if no same-gender member available.

### Multiple Heir Laws

**Partition**: 
1. Oldest child gets primary title, de facto capital, and any higher titles the capital belongs to de jure
2. Empires distributed to oldest child with fewest empire titles
3. Kingdoms distributed to oldest child with fewest empire+kingdom titles
4. Duchies distributed to oldest child with fewest empire+kingdom+duchy titles
5. Counties distributed to oldest child with fewest county titles
6. Baronies go to whoever holds their de jure county

Deceased child's primary heir takes their place. Primary heir vassalizes other heirs unless ranks equal.

**Confederate Partition**: Like partition, but automatically creates new titles at no cost beforehand (same rank as primary title).

**High Partition**: Like partition, but primary heir takes half titles in each step first (rounding up if odd).

Fallback: If no valid heirs exist, titles go to liege (if vassal), liege's vassal (if independent), or liege's courtier (if no vassals).

## Title Succession

Individual title succession laws (elective variants) can override realm succession. Options restricted by rank, culture, title, and government. If primary title has individual succession law, its de facto capital goes to primary heir by realm succession instead.

Title Men-at-Arms (tied to specific titles) move with the title on succession.

## Title Claim Inheritance

Gender law determines whether sons, daughters, or both inherit parental claims. Upon succession, eligible children gain pressed claims on titles they didn't inherit/vassalize. If parent held pressed claims, unpressed claims are inherited instead (unpressed claims can't pass down but revert if pressed in war).

- **Male/female-only**: Only sons/daughters inherit
- **Male/female preference**: Both inherit
- **Equal**: Both inherit

Faith's gender view determines implicit claims during parent's lifetime (male-dominated: sons; female-dominated: daughters; equal: both). Deceased child's placeholder receives implicit claims if appropriate sex.

## Other Inheritance

Primary heir inherits all gold, men-at-arms, and artifacts.

Unlanded heir who inherits duchy+ title automatically usurps a county (preferably de jure capital). Newly landed characters receive complimentary men-at-arms based on income.

Heir receives portion of late ruler's legitimacy:
- 25% if heir was landed
- Greater percentage if heir was unlanded (based on birth order and gender; legitimacy loss negligible for first child of preferred gender)

## Abdication

Abdication entails renouncing all titles (triggered by losing tyranny war or level 3 stress mental break). Abdicator loses -500 Prestige but gains pressed claims on all former titles.

## Tips

- Feudal rulers risk realm-splitting under Confederate Partition; adding "Feudal Elective" succession to primary title helps
- Dynasty head can disinherit dynasty members (costs Renown/Prestige)
- Primary heir always inherits all holdings within capital county
- Under partition, all capital duchy titles go to primary heir if all other heirs expect duchy+; same for kingdom
- Granting heirs their titles in advance prevents other heirs from inheriting claims on them, reducing succession infighting
- Monasticism faith allows requesting characters age 9+ to take vows, disqualifying them from inheritance
- Characters with Czech/Slovien culture unlock House Seniority at any Crown Authority (Table of Princes innovation)
- Aragonese/Basque/Catalan characters unlock High Partition and Equal Cognatic law at High Crown Authority (Visigothic Codes innovation)

## Notes

- Title display order in character screen: primary first, then higher tiers, then same-tier by possession length (oldest first)
- Several cultures get advanced succession laws early via Cultural Innovations
