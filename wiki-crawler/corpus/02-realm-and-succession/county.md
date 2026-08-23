---
title: County
category: realm-and-succession
tags: [county, realm-and-succession, popular, control]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/County]
---

A Count is a character who controls at least one County. It is the second title rank available and the lowest rank that is playable. On the map, the territory of a county will contain multiple Baronies and cannot be altered. Each county belongs to a de jure Duchy, which also cannot be changed.

## Popular opinion

Popular Opinion represents the sentiment of the populace towards the county's direct owner. If Popular Opinion is negative, Populist or Peasant Factions can form in the County.

Each county has a culture and faith. If the ruler who owns the county title has a different faith, it will lose up to -45 Popular Opinion depending on faith hostility and the county's faith's Fervor. If the ruler who owns the county title has a different culture, it will lose up to -15 Popular Opinion depending on Cultural Acceptance and whether they speak the county's culture's language.

A county's culture and faith can be converted by assigning the relevant Councilor Task. Note that the conversion has to be completed in one sitting; progress will be lost if the councilor assigned to the conversion task is reassigned to another task or County.

Offensive wars that last more than 6 months add -0.5 Popular Opinion. This modifier will gradually decay at +0.5 per month after the war ends. If another offensive war is started before the penalty decayed completely, there is no grace period and the penalty will begin to accumulate immediately.

## Control

Control represents the power a landed Count has over their County and ranges from 0 to 100. It can be decreased from events, baronies being captured in sieges (unless title holder has Enduring Hardships perk), or being forcefully seized (-75). Control increases at a rate of 0.1 per month and can be increased faster with the Increase Control in County councilor task.

Every point of Control below 100 brings the following penalties:

- -1% Tax
- -0.5% Levies
- by +0.6% Danger
- -1% County Fertility

If the title holder has the Absolute Control perk when Control is 100 it will read as Absolute and the county will provide an additional +10% Taxes and +5% Levies.

## Development

Development is the measurement of technological advancement and general infrastructure in a county and ranges from 0 to 100. Each point of development increases a county's Supply limit by +150. The average development of counties following a culture will affect that culture's adoption rate of innovations by 0.02 per average level.

If the county is ruled by a Feudal, Clan or Administrative ruler, each point of development also provides +0.5% Taxes and Levies.

Development levels of 10/20/40 or higher also give increasing penalties to the Hunt success chance in the county.

### Development growth

Increasing county development by 1 requires accumulating 100 development growth.

Development radiates outwards from high-development counties to all other counties connected by a land route at 0.1 per difference in development level between these two counties.

Development growth can be most significantly increased via the steward's Increase Development in County task in the council. However, when performing this task an existing development penalty decreasing monthly development growth from it is also applied. The maximum penalty is reached at 10 development, but each era has a civic innovation that will raise the development level at which it is reached: 20, 35, 55, and finally 90. The steward's culture must know these innovations for them to apply, your character's culture and the culture of the county are irrelevant (may not be working as intended as there is currently also a UI bug).

The monthly development growth from the Increase Development in County task is calculated as follows:

- ( 0.1 + 0.175 * Councilor stewardship ) * (1 - existing development penalty)

existing development penalty is capped at 87.5%:

- existing development penalty = min( 0.875, development/100 * 9.13 * Innovation development )

Innovation development applies only if your steward's culture knows the following civic innovations:

- Public Works = 0.5
- Communal Government = 0.2856
- Urbanization = 0.1818
- Renaissance Thought = 0.1111

In addition to not being able to research these innovations past tribal era, tribals also get a x0.5 penalty to development growth increase. The penalty can be avoided by having a feudal liege, vassal or lower rank neighbor. It's not clear if it is working completely as intended.

Development can also be increased by +0.3 monthly in your realm capital through the centralization perk in the stewardship lifestyle or by certain special buildings, but it is still a fairly slow process. Development growth receives positive modifiers from economic buildings, civic innovations (one every era for +10% Development Growth), the 3rd erudition legacy (+20% Development Growth). Terrain can provide a positive or negative modifier, same as event modifiers such as corruption. Modifiers are applied additively after the penalty has been subtracted.

#### Sources of development growth:

|  | monthly development growth |
|---|---|
| From neighbors | +0.1 per difference to neighbors |
| Increase Development in County councilor task | see above |
| Court gardener | +0.1 to +0.7 Development growth in realm capital |
| Buildings | varies |
| Artifacts | varies |

## Corruption

Corruption includes various negative modifiers that can appear for 10 years in a County if Control falls below 35% or the title holder is in Debt for more than 3 months. They can also be added for 5 years by the Collect Taxes councilor action if the Steward has low skill (Stewardship). A county can have up to 3 Corruption modifiers at the same time. Corruption modifiers can be removed by the Marshal task "Increase Control"; one Corruption modifier can be removed by this task immediately if Control is at 100, at the cost of -25 Control.

| Modifier | Effects |
|---|---|
| [Bandits Running Rampant icon] Bandits Running RampantBandits roam freely in the County | -20% Holding Taxes -50% Monthly Development Growth |
| [Deserting Levies icon] Deserting LeviesLevies are deserting in great numbers in this County | -30% Levy Size |
| [Distrust of Courts icon] Distrust of CourtsThere are not enough courts to sit in judgement in peasant cases in this County | -25 Popular Opinion |
| [Incompetent Tax Collection icon] Incompetent Tax CollectionTax collection efforts are failing in this County | -40% Holding Taxes |
| [Inefficient Census icon] Inefficient CensusWe have no idea who or how many people live in this County | -20% Holding Taxes -30% Garrison Size |
| [Lack of Sheriffs icon] Lack of SheriffsThere are not enough sheriffs to handle all the territory in this County | -20% Holding Taxes -30% Monthly Development Growth -10 Popular Opinion |
| [Lackluster Administration icon] Lackluster AdministrationWe can no longer fund the proper administration of the County | -50% Levy Reinforcement Rate -1 Monthly Control |
| [Smuggling Rings icon] Smuggling RingsSmugglers are running rampant throughout the County | -30% Supply Limit -30% Monthly Development Growth |
| [Thieves Guild icon] Thieves GuildA thieves' guild is operating freely in this County | -10% Holding Taxes -80% Monthly Development Growth |
| [Uncooperative Guilds icon] Uncooperative GuildsThe local guilds are reluctant to cooperate with us | +25% Building Construction Time +25% Building Construction Cost |
| [Unsafe Highways icon] Unsafe HighwaysThe highways of this County are less safe than wandering through the forest at night | -20% Monthly Development Growth -10 Popular Opinion |

### Fomented Revolts

Fomented Revolts is a form of corruption that can only be created by characters who have a Yamen Grievance Drum estate upgrade at level 3 or 4. They come in 3 levels of severity depending on how much the character who uses the interaction pays.

| Modifier | Monthly Control | Popular Opinion | Development Growth |
|---|---|---|---|
| [Peasant Outcry icon] Peasant OutcryPeasants are voicing their concerns under foreign influence in this County | -0.1 | -25 |  |
| [Peasant Outrage icon] Peasant OutragePeasants are agitated by foreign agents and refuse to work in this County | -0.25 | -50 |  |
| [Peasant Riots icon] Peasant RiotsPeasants are instigated by foreign propaganda into rioting all over this County | -0.5 | -100 | -25% |

## County Fertility

County Fertility affects Herd. Things like steppe season, Terrain, Holding type, and more affects County Fertility & Fertility Growth.

## Siberian permafrost

Counties in the region of Siberia are affected by Siberian Permafrost, which affects the county differently depending on where its owner's culture has the Tribes of the North tradition.

| [Yes] Tribes of the North tradition | [No] Tribes of the North tradition |
|---|---|
| -6 Monthly Development -60% Building Construction Cost in Forest and Taiga terrain +6 Defender Advantage +1 Building Slots | -6 Monthly Development +600% Building Construction Cost in Forest and Taiga terrain -6 Monthly Control |

Feudalizing the county's holding costs 2500 Gold but removes the permafrost.

## References

Mechanics

| Characters | Characters • Attributes • Traits • Resources • Modifiers • Lifestyle • Family • Dynasty • Schemes • Hooks • Activities • Artifacts • Interactions • Travel • Adventurers • Prisoners |
|---|---|

| Realm & Governance | Council • Court • Power sharing • Subjects • Succession • Government • Laws • Decisions • Titles • Barony • County • Buildings • Royal court • Domiciles • Great projects |
|---|---|

| Warfare | Warfare • Casus belli • Alliance • Army • Hired forces • Knights • Duel • Situations |
|---|---|

| Culture & Faith | Culture • Traditions • Innovations • Form of Address • Faith • Doctrines • Tenets • Holy sites |
|---|---|

| Meta | Modding • Patches • Downloadable content • Developer diaries • Achievements • Jargon • Bookmarks • Interesting characters • Ruler Designer • Game rules |
|---|---|