---
title: Holy War
category: religion-and-culture
tags: [holy, war, religion-and-culture, battles]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Holy_war]
---

Warfare is the most straightforward way of expanding a character's Realm, using armies to take titles or subjects by force. All wars require a Casus Belli, which determines the consequences for each side winning, losing, or reaching a white peace. A character cannot declare war while in Debt. They also cannot declare war while their armies are raised unless they have Nomadic government. If a vassal becomes independent it leaves any war started by its liege. After a war, the allies of both sides 

## Battles

### Combat phases

Battles start when two hostile armies enter the same Barony. At the start of any battle, the terrain's Combat Width decides how many troops are able to fight each other at the same time. Each battle goes through 4 phases:

- Maneuver Phase (2 days): The armies prepare for battle and the Commanders make their initial Advantage rolls.
- Early Battle Phase (12 days): The armies fight and inflict damage upon each other daily and cannot retreat. If an army is defeated in this phase, all Routed Casualties become Fatal Casualties. This will lead to the defeated army being completely destroyed. Oddly, the first day of fighting would have Routed Casualties increase, but the number of armies shown will not decrease.
- Late Battle Phase: The armies keep fighting and keep inflicting damage upon each other each day until either all soldiers on one side run out of Toughness or one side decides to retreat. If an army retreats, all remaining soldiers become Routed Casualties.
- Aftermath Phase (3 days): The winning army gives chase to the defeated army and attempts to turn Routed Casualties into Fatal Casualties. When the phase ends, the defeated army moves into an adjacent Barony with all Routed Casualties and cannot be given orders until it finished traveling a couple of Baronies away, but will travel slightly faster than controlled armies. If all Routed Casualties are turned into Fatal Casualties, the army of the defeated side will instead be completely annihilated.

### The advantage modifier

When combat starts, the Advantage, a modifier that lasts the entire battle and increases the damage of all troops on either side, is calculated for both sides. Advantage can come from traits, terrain, buildings or the Martial skill of the Commander. Each Commander will also make a d10 roll every 3 days in an attempt to increase their Advantage, and the roll can be affected by various modifiers and traits. Each point of Advantage increases an army's Damage depending on game rules. Starting Advantage can be affected by the following:

- +30 if army is defending across a strait
- +20 if army is defending across a large river
- +10 if army is defending across a river
- +10 if Pagan combat advantage
- +5 if liege is leading the army
- +5 if Never Back Down martial lifestyle perk
- +5 if Chivalry focus martial lifestyle focus
- -10 if realm is in debt
- -10 if army is gathering
- -10 if army is low on supplies
- -25 if army is out of supplies
- -30 if army is attacking across sea

### Capturing commanders

A defeated commander may be captured upon defeat in battle. The base chance that the enemy commander is caught is 10%, represented by two chance "scores" in the game script, 90 for escape and 10 for capture. These scores are affected by various factors, and should not be treated as percentages, as their total is not always 100.

| Condition/Factor | Effect |
|---|---|
| Commander has Stalwart Leader Perk (player) | +100 to escape score |
| Commander has Stalwart Leader Perk (ai) | +30 to escape score |
| Prowess | Capture score is multiplied by (30 - prowess score) ÷ 30, with a minimum of 0.1. E.g. a character with 10 prowess would end up with 66% of the total capture score |
| Has the trait Craven | Capture score is halved |
| Army is stackwiped | Escape score is divided by 5 |
| Has the trait Brave | Capture score is doubled |
| Has the trait One-Legged or Maimed | Capture score is tripled |

### Siege

A siege is the main way of gaining War Score and happens automatically when a non-raiding army stops moving in a barony that has a Fort Level. Each such holding has a Garrison, and a siege will only start if the number of Soldiers in the army exceeds it. If the besieging army is ordered to move and there is not another army in the same barony that exceeds the defender's Garrison the siege will end and all siege progress will be lost.

If the siege progresses completely then the barony is occupied. When a barony is occupied it will appear with stripes of its owner and occupier on the map, will produce no Taxes, Levies, Control or Development, and neither the owner nor the occupier will be able to construct or upgrade holdings and buildings. Its Garrison is reset to 25 but will replenish based on the Garrison Reinforcement Rate. County control will also decrease by 40, increased to 80 if the besieger's dynasty has the final Pillage legacy and completely negated if the defender has the Enduring Hardships lifestyle perk.

Baronies that do not have a Fort Level cannot be sieged but will be automatically occupied if every barony in the same county that has a Fort Level is occupied. When a barony is occupied the War Score will shift towards the occupier depending on how big their realm is relative to the captured barony, with additional score if said barony fulfills objectives.

The besieger suffers 1% Attrition per month of their total army while they are besieging. Being attacked while besieging a Fortified Holding will make the besieger the attacker of the battle, conferring any terrain defensive bonus to the other army instead. There is also an additional Advantage penalty for fighting in the same Barony as a Fortified Holding.

All available Loot will be given to the besieger, and grants the holding a "Recently Looted" modifier.

#### Siege progress

During a siege, a Siege Progress bar will slowly increase both on the world map and when the siege is selected. When it fills completely, the barony will be occupied. The amount of Siege Progress needed is 100+75 per Fort Level. It is then reduced by a percentage equal to how many soldiers are currently in the Garrison out of the potential maximum - for example if only half of the maximum Garrison is present the barony will require only half of the usual Siege Progress to the occupied.

Siege Progress is mostly gained by Daily Siege Progress, which accumulates each day the siege is on-going. Daily Siege Progress is 1+0.05 for each 200 besieging Soldiers that exceeds the Garrison. Siege weapons men-at-arms contribute additional Daily Siege Progress. Certain traits and other modifiers can add Daily Siege Progress contribution to men-at-arms that do not ordinarily provide it, or increase the contribution of those that do. Depending on Fort Level and siege weapon men-at-arms in the besieging army, there might be penalties to Daily Siege Progress, but Daily Siege Progress cannot be reduced below 0.5 per day.

| Siege WeaponsFort Level | None |  |  |  |  |
|---|---|---|---|---|---|
| 1-3 | 100% | 100% | 100% | 100% | 100% |
| 4-5 | 70% | 100% | 100% | 100% | 100% |
| 6-10 | 50% | 70% | 100% | 100% | 100% |
| 11-15 | 35% | 50% | 70% | 100% | 100% |
| 16-30 | 25% | 35% | 50% | 70% | 100% |
| 31+ | 17% | 25% | 35% | 50% | 70% |

#### Siege statistics

In addition, during a Siege, the defending fort has three statistics: Supplies, Sickness, and Walls, each of which can be in one of three incremental stages. Stage 1 is the starting position.

| Statistic | Stage 1 effects | Stage 2 effects | Stage 3 effects |
|---|---|---|---|
| Walls | None | One-time reduction of Morale by 5% of original total | One time reduction of Morale by 15% of original total |
| Sickness | None | +10% Daily Siege Progress | +20% Daily Siege Progress |
| Supplies | None | -10% Time Between Siege Events Can assault the Fort with 2.5% daily casualties | -30% Time Between Siege Events Can assault the Fort with 1% daily casualties |

A Siege Event can happen every 20 days (shortened to 14 days with Military Engineer commander trait and also by 10%/30% depending on how much the walls are breached)), which can increase the stage.

| Siege Event | Weight | Effect |
|---|---|---|
| Stalemate | 20 | No effect |
| Desertion | 20 | +5.0 Siege Progress |
| Starvation | 15 | Changes Supplies by one stage |
| Disease Outbreak | 15 | Changes Sickness by one stage |
| Breach | (30 * siege weapon tier) - (fort level x 2) | Changes Walls by one stage |

Once the walls have been breached, the siege icon on the map will change to show a ladder and the holding can be assaulted. Assaulting will add a large amount of daily Siege Progress at the cost of casualties. For every 100 Soldiers besieging (rounded up), Daily Siege Progress increases by 0.2. Hovering over the button to assault the holding will display how it will affect siege progress and casualties.

Strategy

As can be seen, having appropriate Siege Men-at-Arms is vital to conducting sieges effectively. Simply adding more Soldiers to a siege has effectively negligible increase on the time to success. Even worse, if there are no Siege Men-at-Arms at all, breaching the Walls becomes impossible, and an army is unable to Assault the Fortified Holding, leaving it stuck in the slow and damaging Siege. This is particularly notable for Tribal characters who can lack access to any Siege Men-at-Arms at all, and therefore have very good reason to focus on the Onager innovation. The Sappers Perk in the Military Strategist Lifestyle helpfully adds +0.1 Daily Siege Progress to a number of Men-at-Arms units which otherwise lack it, and is therefore incredibly useful to Tribal characters, although notably it does not add a Siege Tier to these units. Once a Siege Men-at-Arms unit has been unlocked, the Engineered Destruction Perk, in the same Lifestyle, is usually more powerful, increasing Daily Siege Progress on Siege Men-at-Arms units by 40%. Even a simple Size 1 Onager unit will go from +1.0 to +1.4 with this, an increase of +0.4, the same that Sappers will give to a Size 4 Armoured Footman unit. Such is the strength of Engineered Destruction, and the fact it is applied Realm-wide rather than per Commander, that it can be well worth diverting into the Strategist Lifestyle just for this perk.

The maths of the formula means that additional Siege Men-at-Arms have diminishing returns. With a Defender Morale of 400, increasing Daily Siege Progress from 1.0 to 2.0 decreases the length of the Siege (ignoring Siege Events) from 400 days to 200 days, a 200 day drop, but increasing Daily Siege Progress from 2.0 to 3.0 only decreases the length of the Siege from 200 days to 134 days, a 66 day drop. In addition, as only a single Men-at-Arms unit is needed to unlock a particular Siege Tier, players may wish to consider spreading Siege Men-at-Arms units across multiple sieges rather than concentrating them on a single siege.

### Prestige and fame gain on victory

Victory of a battle might grants prestige, fame, piety, or devotion. You gain fame if you are the war leader and enemy is either the war leader or ally in the war. Otherwise you get prestige and devotion, this includes cases such as when you fight as an ally, or when you fight against your enemies' vassal.

## War score

War score is a measure of which side is winning a war. It ranges from -100 to +100, each point added to one side being subtracted at the same time from the other side, e.g. if one side has 25 War score, the other side will have -25 War score. War score is gained by winning Battles, occupying Holdings, taking important prisoners and especially having control of the Casus Belli's Objective, or the "War Target". Even though the game doesn't define the term "War Target", it appears to correspond to whether either side has possession of at least one county in the de Jure title being fought over. If either side controls the entirety of the de jure title being fought over, they accumulate war score every month. If the other side takes control of at least one of these counties, the war score gained from control resets to 0 but will return to its previous level if the county/ies are recaptured. If neither side controls all de jure disputed land, there is no gain from control. For example, a war for the Duchy of Lancaster in England means that there are 4 counties that are at claim. If the attacker seizes all 4, they accumulate 1% per month of war score.

After a certain amount of time, the defenders will gain score if the attackers have failed to capture any of these counties. Note that this does not apply in wars where the claim is on the highest title in that realm. For example, a claim on England will not accumulate a control score as long as the attacker takes even a single county; if they were to take them all, they would automatically win by full occupation unless the Empire of Britannia has been created and is the liege of the holder of the title of Kingdom of England.

| Objective | Bonus war score |
|---|---|
| Capturing enemy ruler | +100 |
| Capturing enemy heir | +50 (primary heir)+25 (secondary heir)+10 (tertiary heir) |
| Occupying enemy capital | +10 |

The benefits given by winning battles is based on the size of the losing army relative to its total soldier count. The benefits given by occupying holdings correspond to a percentage of the total holdings the defender has, both inside and outside the war target. Against rulers battles can give up to 50% war score. Against adventurers there is no limit and if the adventurer runs out of men-at-arms the war score will shift all the way in favor of the ruler.

### Ending the war

- White Peace At +30 War score, the winning side can call for this.
- Enforce Demands: At +100 War score, the winning side can enforce their demands on the losing side.
- Surrender Players can always Surrender to the opposing side, ending the war and enforcing the opposing side's demands on themselves. Alternatively, at -100 War score, the losing side must surrender to the winning side. This can be modified by Peace Acceptance, particularly with the Peacemaker Lifestyle Perk. The AI will also eventually surrender to the player when the player has +100 war score, preventing the player from taking additional captives or inflicting additional damage to their realm.
- War Condition invalidated: sometimes the war can end inconclusively, usually due to the Casus Belli becoming invalidated. Each CB have their own invalidation conditions. E.g. if the CB is for a county and the defender lose control of the county, the war has no reason to continue.

### War contribution

Wars where either the attacker or the defender has allies keep track of the percentage of War score that was provided by each ally's armies. When the war ends, a certain amount of Gold, Prestige or Piety is shared among all allies based on their War Contribution.

If a war lasts at least 2 years and one of the allies has 0% War Contribution, it will lose -20 Opinion with the war leader and have to pay Gold or Prestige or promise to earn War Contribution within a year. Breaking the promise will result in losing a Level of Fame as well as -50 Opinion with the war leader.

## Holy wars

Holy Wars are wars started with one of the Holy War casus belli. Unlike other wars, Rulers of the same Faith as the defending Ruler can join the war without requiring an Alliance. A Ruler targeted by a Holy War gains a character interaction to convert to the attacker's Faith in order to end the war in White Peace at the cost of 100 Piety and 3 Levels of Devotion.

### Great holy wars

Great Holy Wars can only be declared by a Head of Faith whose faith has the Warmonger, Armed Pilgrimages, Struggle and Submission tenets or Special Doctrines such as Rightful Rulers of the World and their Head of Faith is not imprisoned. They can only target Kingdoms ruled by a character of a different Faith. If victorious, all Titles within the targeted Kingdom are seized and divided between the attackers based on their War Contribution. Great Holy Wars can be Directed or Undirected. Great Holy Wars do not cause Vassal Opinion loss no matter how long they last. A faith must have at least 75% fervor to launch a Great Holy War.

Characters of the attacking Faith who pledge military support can also choose a Beneficiary, an unlanded and non-heir character of their Dynasty who will receive titles in the targeted Kingdom proportional to their War Contribution.

During Great Holy Wars, there is no option for White Peace and capturing and imprisoning the opposing war leader or its Heir will not grant War score. If the attacking Faith wins, its Fervor will decrease by -30 while the defending Faith's Fervor will increase by +25%. If the defending Faith wins, the attacking Faith will lose -25 Fervor.

Rulers who contribute to a Great Holy War and knights in the armies that fight such a war will gain the Crusader trait if Christian, Mujahid trait if Muslim, and or Religion-specific versions of Warrior of the Faith trait for other Religions. In addition, if the character had the Excommunicated trait, it is removed.

AI rulers are less afraid of armies that outnumber theirs during Great Holy Wars.

#### Directed great holy wars

Directed Great Holy Wars can be declared by Temporal Heads of Faith. If victorious, the Kingdom is granted to the Head of Faith. Rulers of the same Faith can join forces with the Head of Faith, and based on their War Contribution, may gain Piety or Titles in the conquered Kingdom if victorious.

#### Undirected great holy wars

Undirected Great Holy Wars can be declared by Spiritual Heads of Faith. When declared, a preparation phase starts, during which Rulers of the attacking and defending Faiths can either donate gold or pledge military support to their side.

Each Undirected Great Holy War will have a War Chest, to which characters of the attacking Faith can donate Gold in order to receive Piety equal to half of the amount donated. Donating significant amounts will also grant bonus Opinion with the Head of Faith. When the preparation phase ends, 20% of the War Chest's value will be divided among all rulers who pledged military support for the attacking Faith. The rest will be divided among all rulers who pledged military support if their Faith wins.

During the preparation phase, characters belonging to the Faith of the attacker or the defender can pledge military support. Characters who pledge military support may gain a share of the War Chest's value and will end all wars against characters who also pledged military support. Upon pledging, characters of the attacking Faith will gain Piety and the War Chest will gain Prestige and Piety depending on their Primary Title rank:

| Rank | Piety | War Chest Prestige | War Chest Piety |
|---|---|---|---|
| Baron | 30 | 250 | 75 |
| Count | 60 | 500 | 150 |
| Duke | 90 | 1000 | 300 |
| King | 120 | 1500 | 600 |
| Emperor | 150 | 3000 | 1200 |

A character can withdraw their pledge for military support after making it, but doing so will cause them to lose one Level of Devotion.

In addition, during the preparation phase, characters who pledged military support can spend Piety to change the targeted Kingdom. This must be done at least 101 days before the start of the Holy War.

If, during the preparation phase, the head of faith calling for the great holy war dies for any reason, the great holy war will not be called off.

Once the Preparation Phase ends, the war starts if the projected attacker strength is less than 33% of the projected defender strength. If the attackers are victorious, the Kingdom is granted to the attacker that had the highest War Contribution. During both war and the preparation Phase, attackers may donate Gold to the War Chest.

#### Unlocking Great Holy Wars

To unlock Great Holy Wars a Faith must:

- have the right Doctrines
- Head of Faith must exist and not be imprisoned
- there must be at least 35 counties in the world following the Faith
- fervor has to be above 65%
- at least ten years must have passed since another Faith unlocked Great Holy Wars.

If those conditions are met, a Faith will unlock Great Holy Wars after year 1100 but they can be unlocked at any point earlier if two Holy Sites are in a realm whose top liege is not of the same religion. Crusades and Jihads can be unlocked earlier if certain conditions are met.

| Faith | Minimum year | Condition |
|---|---|---|
| Catholic | 1095 | Top liege of Jerusalem is not Christian |
| Catholic | 1000 | Byzantine emperor or top liege of any of these counties is not Christian: Ankyra, Athens, Constantinople, Corinth |
| Catholic | 800 | The top liege of any of these counties is not Christian: Cologne, Halberstadt, Paris, Venaissin, Toulouse |
| Catholic | - | Top liege of Rome is not Christian |
| Islam | - | After Christianity has unlocked, and any holy site is in a realm whose top liege is not Muslim OR the top liege of Jerusalem or Mecca is not Muslim |
| any faith | - | After both Christianity and Islam have unlocked, and any holy site is in a realm whose top liege is of Hostile or Evil faith. |
| any faith | 800 | Any two holy sites are in a realm whose top liege is of a different religion. |

#### Great Holy War Weights

Great Holy Wars have a multiplier for AI targeting of 100 for a key religious holding (Jerusalem for Catholics and Jews, Mecca and Medina for Muslims), 75 for the kingdom where someone who made a Human Sacrifice of the Head of Faith came from, 50 for kingdoms with a holy site, 40 for kingdoms in heartland regions, 30 for frontier regions, 20 for fringe regions, and 10 for stretch regions. Note this means all other kingdoms would have a multiplier of 1. If the Head of Faith is landed, this is divided by the distance from the Head of Faith. If not, it is divided by the distance from the primary religious site (e.g. Rome). There is also a multiplier of 20 if someone of the same faith holds the kingdom title, but does not possess enough of the kingdom. Great Holy War Weights can be found in game\common\script_values\02_religion_values.txt.

## Raiding

Raiding is the process of attacking the Holding of another character without requiring to be at war with them in order to gain Loot. In order to raid an army must be raised as raiders, which requires at least one of the following:

- Unreformed faith
- Tribal government
- Practiced Pirates tradition
- Ghazi Status tax decree
- Legacy of Piracy dynasty modifier
-  Frontier administration
-  Nomadic government
- Wanua government
- Meritocratic Khanate government

Raiders will carry loot based on the army size and they cannot embark unless their culture has unlocked the Longships or West African Canoes innovation or has the Practiced Pirates tradition. While a raiders army is selected, each holding near borders will display how much loot can be obtained. While raiding, the army cannot move, allowing the attacked character to raise an army against them if possible. If a raider army is defeated before returning inside its own borders all loot will be recovered. Maintenance cost for armies raised as raiders is reduced by 50%. Each army raised as raiders will have a Raid Intent, which determines what will the loot be converted into. Most raid intents have additional bonuses but those are reduced to half if the duchy has a Marches duchy building and completely eliminated if the building is upgraded.

| Intent | Loot conversion | Loot conversion | Loot conversion | Raid speed | Raiders speed | Effects | Requirements |
|---|---|---|---|---|---|---|---|
| Pillage | 100% Gold | 100% Gold 100% Prestige | 50% Gold 100% Herd | 100% | 100% | -1.5 Prestige per Loot if not Tribal, Wanua or Nomadic |  |
| Adventure | 100% Gold 100% Prestige | 100% Gold 100% Prestige | 50% Gold 100% Herd | 80% | 50% | No Hostile County Attrition +300% Army Loot Capacity | Longships innovation |
| Capture |  Unavailable | 50% Gold | 25% Gold 50% Herd | 70% | 75% | +15% Chance to imprison characters |  |
| Terrorize |  Unavailable | 100% Prestige 10% Dread | 100% Prestige 10% Dread | 40% | 100% | +30% Chance to be offered to sack the holding 25% Chance the county loses 5 Fort Level and 75% Garrison for 5 years 25% Chance the county loses 1 Development 25% Chance the holding loses 1 building | Scorched Earth or No Quarter legacy |
| Plunder |  Unavailable |  Unavailable | 100% Gold 150% Herd | 40% | 50% | 2% Chance to gain an innovation |  Culture head |

Once a Holding has been Raided it cannot be Raided again by the same enemy for 5 years, during which time the Holding will have -50% Taxes, +50% Building Construction Time and -10% Development Growth. If the raided Barony is a Ruler's Realm Capital, raiding may capture or kill courtiers or family members. Holdings that have been Raided will have a torch icon above them when a raider army is selected. Realms at truce with cannot be raided.

If a Commander has raided at least 20 times, each raid has a chance to grant them the Raider trait equal to the amount of times they raided.

If a ruler is the army's Commander after the Holding is raided, there is a 30% chance they will gain the option to sack its County. The chance is increased to 50% if they have the Raider trait. Sacking the County presents at least one, sometimes two options. A player can always sack for additional treasure, granting more Gold and Prestige while the County will gain -40 Development Progress. When sacking a feudal holding, if the raider's capital has under 15 Development, they are also presented with a second option to capture slaves for their capital. Choosing this option will increase Development progress in the raider’s capital by +40, decrease the sacked county’s development by -1, and decrease sacked county’s development progress by -80. Choosing either option will also give the County the Recently Sacked modifier for 20 years, which prevents it from being sacked again and gives it +20 Popular Opinion. Sacking a County will grant +10 Stress if the character has the Compassionate or Forgiving traits.

Raided rulers gain a decaying -15 Opinion (+1.47/year) towards the owners of the raiding armies.

If the Northern Lords DLC is installed rulers who meet certain requirements have a 20% chance to be offered to trade instead of raiding. The chance is increased to 40% if the character belongs to the North Germanic culture group or has the second Adventure dynasty legacy. If the offer is accepted the army will gain 10 Loot and +20 Opinion with the realm owner but will not be able to raid them for 5 years. In addition the previously raided County will get a +20 Popular Opinion modifier for 5 years. To be offered to trade, the following requirements must be met:

- At peace
- Leading the raiding army as a Commander
- Raiding a Castle holding
- Either the Longships innovation or the second Adventure dynasty legacy

Raiding armies can fight barterer armies to take their Barter Goods as loot.

## Capturing characters in a holding

Characters present in a holding which has just been occupied or raided have a chance to be imprisoned by the besieging force. The following conditions exclude characters from being capturable:

- The besiegers have defeated the defender's army, but the defender's army has not yet retreated to a different province
- The character is imprisoned in the barony

For eligible characters, the base chance to be captured is 35%. Each point of Intrigue reduces the chance by 1%, up to a maximum reduction of 20%, and each point of Prowess reduces the chance by 0.5%, up to a maximum reduction of 15%. The third Pillage legacy effect adds 20% to this chance.

If the occupying force is a peasant army, or the target is undesirable, a captured character will instead be killed. A target is desirable if any of the following is true:

- They are landed
- They have at least one parent
- Their spouse is landed
- Any close family member is landed
- They have a high skill rating in diplomacy, martial, stewardship, intrigue or learning
- They have a physician lifestyle trait
- They have a mystic lifestyle trait

## Initial wars

The following wars are present at the start of each game. Mogyër Confederation will also start at war with Bulgaria using the Migrate to Pannonia casus belli if the Hungarian Migration game rule has been set to Immediate.

| Attacker | Defender | Casus belli |
|---|---|---|
| Aghlabid | Byzantine Empire | Conquer Duchy |
| Hadithan-Ana | Abbasid Empire | Invade Kingdom |
| Asturias | al-Andalus | Claim |
| Saffarid | Tahirid | Invade Kingdom |
| Tulaytulah Burtughal | al-Andalus | Independence |
| Italy | Apulia | Conquer Duchy |
| Jórvík Uppland | Northumbria Mercia Wessex | Varangian Adventure |
| The Suðreyjar | East Anglia Mercia Wessex | Varangian Adventure |
| The Suðreyjar | Northumbria | Varangian Adventure |

| Attacker | Defender | Casus belli |
|---|---|---|
| Seljuk Empire | Byzantine Empire | Claim |
| Norway | England | Invade Kingdom |
| Normandy | England | Invade Kingdom |
| Ruhunu | Chola Kingdom | Claim |

| Attacker | Defender | Casus belli |
|---|---|---|
| Jamtaland | Norway | Claim |

## Truce

When a war ends, the attacker and the defender will gain a truce for 5 years. If the former attacker declares war again while the truce is active, they will lose 250 prestige and one level of fame and gain −50 general opinion for 3 years. This will not happen for wars declared via decisions.

- Defensive Negotiations diplomacy perk enables the Purchase Truce interaction
- Flexible Truces diplomacy perk: -25% Truce Time, and no Prestige penalty for breaking Truces

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