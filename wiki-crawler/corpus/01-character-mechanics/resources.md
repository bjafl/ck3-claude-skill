---
title: Resources
category: character-mechanics
tags: [resources, gold, prestige, piety, renown, influence, herd]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Resources]
---

Resources are currencies spent on character actions and realm management. Four core resources (gold, prestige, piety, renown) are universal; others depend on government type.

## Gold

Gold represents liquid wealth reserves. Most rulers start with 18 months of income. On ruler death or abdication, all gold passes to the primary heir regardless of succession law.

### Treasury

Characters with Administrative, Celestial, Meritocratic, or Meritocratic Khanate governments have a second gold storage: Treasury. 95% of vassal income goes to Treasury instead of Gold. Gold can be manually converted to Treasury; each 10 Gold transferred causes ±1 Stress (−1 for Generous, +1 for Greedy).

Treasury is spent on barony constructions, provincial men-at-arms, activities, salaries, great projects, and court expenses. Gold is spent on estate constructions, personal men-at-arms, schemes, and most activities.

The top liege allocates Treasury income percentages to vassals as Gold via the Laws tab. Amount depends on vassal primary rank and Merit. Reallocation costs 200 Prestige and 500 Influence, grants −100 to +30 Opinion for 5 years based on change magnitude. Liege can use Debt Relief interaction on indebted vassals to gain 100 Influence and a 20-year Strong Hook.

### Debt

Occurs with negative gold or treasury. Penalties stack if both are negative. Cannot declare war, counties gain corruption, men-at-arms cannot reinforce, and negative events occur.

| Years in debt | Levy/Reinforce | Dev growth | Vassal/Popular opinion | Courtier opinion | Advantage | Join faction | [Khans] Herd | Conqueror |
|---|---|---|---|---|---|---|---|---|
| 0 | −10% | −10% | −5 | −10 | −5 | +10 | −10% | Yes |
| 1 | −20% | −20% | −10 | −15 | −10 | +20 | −20% | Yes |
| 2 | −30% | −30% | −15 | −20 | −15 | +30 | −30% | Yes |
| 3 | −40% | −40% | −20 | −25 | −20 | +40 | −40% | Yes |
| 4 | −50% | −50% | −25 | −30 | −25 | +50 | −50% | Yes |
| 5 | −60% | −60% | −30 | −40 | −30 | +60 | −60% | Yes |
| 10 | −70% | −70% | −40 | −50 | −40 | +70 | −70% | No |
| 25 | −80% | −80% | −50 | −75 | −50 | +80 | −80% | No |
| 50 | −90% | −90% | −75 | −100 | −75 | +90 | −90% | No |
| 100 | −95% | −95% | −100 | −120 | −100 | +95 | −95% | No |

## Prestige

Prestige represents political capital and social influence. Gained from holding titles (especially high rank), diplomacy skill, and events. Spent on vassal interactions, decisions, and secular wars. Tribal/Wanua rulers spend it on men-at-arms and building construction.

Each prestige gain = same fame gain. Battles and war victories (as attacker/leader) generate additional fame. Losing wars as leader loses fame. Dishonorable acts lose fame levels. Characters can spend fame at inflated price for secular wars if prestige-poor.

"A Life of Glory" Diplomacy lifestyle perk doubles Secular Opinion and Knights effects (including penalties).

### Level of fame

| Fame level | Secular opinion | Knights | Tribal tax | Tribal levies | Max conquest CB | Adopt feudal/clan | Max custom title | Fame | Max contractor rank | [Khans] Herd capacity |
|---|---|---|---|---|---|---|---|---|---|---|
| Disgraced | −10 | −1 | 0% | 0% | None | No | Duchy | 0 | Count | −10% |
| Established | 0 | 0 | 8% | 15% | County | No | Duchy | 1000 | Count | +10% |
| Distinguished | +5 | +1 | 16% | 30% | County | Yes | Duchy | 2000 | Count | +20% |
| Illustrious | +10 | +2 | 24% | 45% | Duchy | Yes | Kingdom | 5000 | Duke | +30% |
| Exalted among Men | +20 | +3 | 32% | 60% | Kingdom | Yes | Empire | 10000 | King | +40% |
| The Living Legend | +30 | +4 | 40% | 75% | Kingdom | Yes | Empire | 25000 | Emperor | +50% |

## Piety

Piety measures religious virtue in the eyes of believers. Gained from religious relations, learning skill, and virtue traits. Spent on church interactions and holy war declarations. Icon depends on character's religion.

### Level of devotion

Each piety gain also progresses toward next devotion level, granting various benefits. Lost by doing actions faiths consider shunned. Characters can pay piety cost with devotion if piety-insufficient. Generated characters and game start characters begin at Dutiful level.

Mandala government rulers inherit predecessor's devotion level and can reach Demigod/Godlike only if predecessor reached previous level and died acceptably. Humility noble family attribute (highest level) can reach Divine.

| Level | Effects | Theocracy tax | Theocracy levies | Max holy war rank | Create holy orders | Consecrate bloodline | Devotion |
|---|---|---|---|---|---|---|---|
| Sinner | −10 Same Faith Clergy (Theo), −5 Same Faith (Lay) | 0% | 0% | None | No | No | 0 |
| Dutiful | — | 15% | 10% | County | No | No | 1000 |
| Faithful | +5 Clergy (Theo), +3 (Lay) | 25% | 20% | Duchy | No | No | 1500 |
| Devoted Servant | +10 Clergy (Theo), +5 (Lay) | 35% | 30% | Duchy | Yes | No | 2500 |
| Paragon of Virtue | +20 Clergy (Theo), +10 (Lay) | 45% | 40% | Kingdom | Yes | No | 4500 |
| Religious Icon | +30 Clergy (Theo), +15 (Lay) | 55% | 50% | Kingdom | Yes | Yes | 8500 |
| Divine | +40 Clergy (Theo), +20 (Lay), +0.1 Renown, +0.2 Legitimacy, +15 Vassal Limit | 65% | 60% | Kingdom | Yes | Yes | 13000 |
| Demigod | +55 Clergy (Theo), +25 (Lay), +0.15 Renown, +0.3 Legitimacy, +25 Vassal Limit | 75% | 70% | Kingdom | Yes | Yes | 17000 |
| Godlike | +75 Clergy (Theo), +35 (Lay), +0.2 Renown, +0.4 Legitimacy, +35 Vassal Limit | 85% | 80% | Kingdom | Yes | Yes | 22500 |

### Monthly piety sources

**Flat gains:**
- Theology Focus: +1.0
- Head of Faith: +1.0
- Per Virtuous Trait: +1.0
- Per Burial Site building level: +1.0
- Humble trait: +0.5
- Learning skill: +0.1 per level

**Percentage modifiers:**
- Zealous trait: +20%
- Cynical trait: −20%
- Theolo gian trait: +20%
- Holy sites (varies by location): +0.1 to +20%
- Dynasty Legacy "Erudition" Level-2: +10%
- Court position "High Almoner": +20%

## Renown

Renown is a secondary piety-like resource gained through legendary deeds and lost through dishonorable acts. Characters with high renown gain benefits. Renown = Dynasty Renown (shared across dynasty) and Personal Renown (individual). Dynasty head has full dynasty renown; family members have reduced amounts.

Only independent rulers gain dynasty renown; vassals only gain personal renown. Renown family attributes affect dynasty renown.

## Influence

Resource for Administrative, Celestial, Meritocratic, Meritocratic Khanate, and Ritsuryō governments. Represents political reach and authority. Gained from being governor, council service, estate upgrades, and allying with powerful families (especially top liege).

### Level of influence

Each influence gain progresses toward next level, affecting political scheme success chance.

| Level | Scheme success | Personal movement power | Change succession law | Influence |
|---|---|---|---|---|
| Impotent | — | — | No | 0 |
| Influential | — | +5 | No | 1000 |
| Persuasive | +5% | +10 | No | 2000 |
| Controlling | +10% | +15 | No | 4000 |
| Authoritative | +15% | +20 | Yes | 8000 |
| Imperious | +20% | +25 | Yes | 16000 |

## Provisions

Resource for adventurers, spent when camp moves. Expended amount depends on men-at-arms size, terrain, and officers. Gained from contract rewards, hunts, visiting holdings, and Gather Provisions decision.

Initial storage: 2500. Increased by camp buildings. Excess converted to gold (1 gold per 20 provisions).

### Low provisions effects

| Provisions | Events |
|---|---|
| 500–67 | −15 opinion with follower or lose leveled gold |
| 66–34 | Every regiment −15% soldiers, +20 stress; follower leaves (non-close family/officer), +40 stress |
| 33–1 | All events +80 stress, −15 opinion all followers; regiment −35%, close family leaves, get Ill trait; follower/pet dies (option to become Cannibal); typhus epidemic (15% regiment losses, one infected) |
| 0 | +100 stress, −25 opinion all followers, −50% soldiers; gain Weak Stomach, Hunger Sickness, Blind, Cannibal, Infirm, Lunatic, −2 Prowess, or death |

## Herd

Resource for Nomadic government rulers. Represents flock of animals, used as currency between nomads, gates Dominance increase, and converts percentage into Horde Riders. Highest-herd character becomes culture head. Every 1000 Herd = +0.5 gold income. Converts to gold on government change.

Herd capacity determined by title rank, fame level, and nomadic capital buildings. Exceeding capacity reduces herd gain to 5% normal. Landless rulers lose 500–⅓ herd every 3 years.

Gained from county Fertility (steppe regions range 0–100). Nomadic rulers reduce fertility to equilibrium; Herder rulers increase it. Equilibrium increases with domain baronies count.

## Barter Goods

Resource for Wanua government rulers. Represents island resources used for army upkeep. Armies can convert to Gold at 2:1 ratio by being raised as barterers and traveling to other rulers' counties.
