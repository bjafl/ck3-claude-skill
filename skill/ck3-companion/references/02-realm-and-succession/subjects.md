---
title: Subjects
category: realm-and-succession
tags: [subjects, vassals, tributaries, lessees]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Subjects]
---

Subjects are rulers who submit to more powerful rulers, providing resources in exchange for protection from attacks. Three subject types exist: vassals (can have vassals and lessees), tributaries (independent with truces), and lessees (clergy with baronies). Tributaries may have their own subjects; vassal-to-tributary conversion is unilateral, but tributary-to-vassal conversion requires tributary agreement.

Subject tithes reduce when the ruler lacks titles that the subject's primary title is de jure part of (Dukes with de jure empire titles exempt):
- No reduction: owning 1 rank above (Kingdom title for Duchy vassal)
- 25% reduction: owning title 2 ranks above (Kingdom title for Count vassal)
- 50% reduction: no de jure title owned

Governments using Treasury resource receive subject tax income as Treasury instead of Gold.

## Vassals

Vassals surrender sovereignty to higher-ranked lieges. They join liege wars (except civil wars against them) but aren't obligated to participate. Lieges join vassal defensive wars unless vassals attack other vassals (Crown Authority may prohibit this). Vassals provide Taxes and Levies based on government type:

- **Administrative/Celestial/Meritocratic/Meritocratic Khanate/Ritsuryō**: Governor efficiency-based
- **Feudal/Sōryō**: Vassal contract-based
- **Tribal/Wanua**: Fame-based with tribal authority minimums
- **Clan**: Opinion-based with crown authority minimums; if liege is Clan, vassal must be assigned to Tax Jurisdiction
- **Nomadic**: Vassal contract-based
- **Theocracy**: Liege devotion-based
- **Republic**: Always 20% taxes and 10% levies

Title grants transfer lower-ranked vassals whose realms fit entirely within the granted title's de jure realm. Vassal borders/flags hide unless vassals selected (player vassals always visible).

### Vassal Limit

Every ruler has a Vassal Limit. Exceeding it reduces all vassal Taxes and Levies by -5% per excess vassal (max -95%). Baron vassals don't count. Exceptions:
- Administrative: title rank plus authority law level
- Nomadic: Dominance law
- Mandala: Devotion level plus Capital Temple Complex building
- Wanua: tribe buildings increase limit
- Extreme AI Conquerors: 500 limit regardless

### Vassal Directives

Rulers can direct vassals to construct specific buildings or convert faith/culture. Directives require one of: Absolute Control perk, Strong Hook, Absolute Crown Authority, Ordained legitimacy, 50+ Opinion, Trusting/Loyal trait, or Friend/Best Friend status. Both having Administrative/Celestial/Meritocratic/Meritocratic Khanate/Ritsuryō government exempts requirement.

### Powerful Vassals

Vassals with Gold/Levies income are "powerful" and expect council seats (-40 opinion if excluded). Numbers by title rank: 3 Counts, 4 Dukes, 5 Kings+. In elective succession, they have more votes and resist sway. Succession law changes require all powerful vassals to have positive opinion, be terrified, or be imprisoned.

### Vassal Stances

Each vassal has a Stance (AI personality-determined) affecting opinion and heir preference. Preferred heir gives +30 Opinion; non-preferred gives -20 Opinion upon succession.

| Vassal stance | Likes | Dislikes | Heir preference | Favored by |
|---|---|---|---|---|
| Belligerent | High authority laws, Duels won, Hunt, Grand Tournament won | Low authority laws, Duels lost, Multiple heir succession | Highest Prowess | High Honor High Vengefulness Low Compassion |
| Courtly | Court positions, New titles, Feast invites | Lowborn titles/spouses, Disinheriting | Highest Diplomacy | High Compassion High Sociability Low Greed |
| Glory Hound | Partition laws, Offensive war victories, Feast invites | High crown authority, Defeats, Lowborn spouse | Highest Martial | Low Compassion Low Honor |
| Parochial | Holdings built/upgraded, Family guardian, Domestic Affairs councilor | High crown authority, Non-trivial wars | Highest Stewardship | High Rationality Low Boldness Low Sociability |
| Zealot | Virtue traits, Temple construction, Learn Language scheme, Pilgrimage | Sin traits, Head of Faith gold requests | Highest Learning | High Vengefulness High Zeal |
| Minor Landholder | Low crown authority | High crown authority, Title revocation | Faith matching or Righteous/Astray; Culture matching or 30%+ acceptance | Always barons |
| Minority | Promote Cultural Acceptance | High crown authority, Faith/Culture conversion | Different culture/faith | Hostile/Evil faith or <30% acceptance |

### Vassal Contracts

Feudal/Clan/Nomadic/Sōryō vassals have contracts determining obligations and rights. Contracts change once per character lifetime (shared between liege/vassal). Up to 4 simultaneous changes allowed. Each desirability point difference costs 20 tyranny (doubled for Normal→High taxes). Weak hooks offset 1 tyranny point; balanced changes prevent additional liege-favoring changes if tyranny already incurred.

#### Rights

| Right | Liege effects | Vassal effects | Requirements | Score |
|---|---|---|---|---|
| Council Rights: Guaranteed | +5 Opinion −2 to powerful vassals | Demand council position without hook |  | +3 |
| War Declaration: Sanctioned | +5 Opinion | Declare war regardless of crown authority −50% casus belli cost vs vassals |  | +1 |
| Title Revocation: Protected | +5 Opinion | Cannot revoke titles | Not Nomadic | +1 |
| Religious Rights: Protected | Cannot demand conversion/convert domain +5 Opinion | +5 Popular opinion | Not same faith; faith lacks Tax Nonbelievers | +3 |
| Jizya Status: Granted | +20 Opinion +40% Tax −40% Levies Cannot revoke title/demand conversion/convert domain | −0.25 Monthly Prestige | Feudal/Sōryō Not same faith Faith has Tax Nonbelievers | +1 |
| Succession Rights: Forced Partition | −5 Opinion | Forced multiple heir succession +25% law change prestige | Feudal/Sōryō | -1 |
| Coinage Rights: Granted | −2% Development growth | +0.3 Development in realm capital | Feudal/Sōryō Coinage innovation | +1 |
| Fortification Rights: Granted | +5% Castle construction −10% Tax | +1 Fort −15% Castle construction −50% Holdings construction | Feudal/Sōryō Battlements innovation | +1 |
| Iqta Grant: Granted | −2% Men-at-Arms recruitment/maintenance +5 Opinion −50% Tax/Levies | −10% Men-at-Arms recruitment/maintenance | Clan |  |
| Marriage Favor: Granted | +10% Tax/Levies +20 Opinion | +150 Prestige if marrying liege's close family | Clan |  |
| Ghazi Status: Granted | +10% Piety +10 Opinion −25% Levies | +10% Piety −50% Holy War Casus Belli −50% Holy War cost +25% other casus belli | Clan Same faith |  |
| Liege War Support: Forced | +15 Opinion | Call liege to war | Nomadic |  |
| Raiding Privileges: Granted | +5 Opinion | Raid fellow vassals | Nomadic |  |

#### Special Contracts

Available with innovations; March requires bordering another realm:

| Contract | Liege effects | Vassal effects | Title rank | Innovation | Government |
|---|---|---|---|---|---|
| Castellan | −50% Levies | −20% Maintenance +20% Levy size/Garrison/Reinforcement +5 Defender advantage | Count | Bannus | Feudal Clan Sōryō |
| March | −50% Tax | −20% Maintenance +20% Levy size/Garrison/Reinforcement +5 Defender advantage | Duke King | Bannus | Feudal Clan Sōryō |
| Palatinate | +5% Prestige −20% Tax/Levies | +20% Prestige +15 Vassal Opinion +10% Scheme success | Count Duke King | Divine Right | Feudal |
| Scutage | +50% Tax −75% Levies | −20% Men-at-Arms maintenance | Duke King | Scutage | Feudal |

#### Obligations

Feudal/Nomadic/Sōryō vassal contracts include changeable obligations. Lowering costs nothing; raising adds +20 tyranny (doubled Normal→High taxes) unless liege lowers other obligation, grants rights, or uses hook.

| Obligation | Exempt | Low | Normal | High | Massive |
|---|---|---|---|---|---|
| Taxes | 0% Tax +15 Opinion +2 Score | 2.5% Tax +10 Opinion +1 Score | 10% Tax +5 Opinion 0 Score | 15% Tax −10 Opinion -2 Score | 25% Tax −20 Opinion -3 Score |
| Levies/Herd | 0% Levies +15 Opinion +2 Score | 10% Levies +10 Opinion +1 Score | 25% Levies +5 Opinion 0 Score | 35% Levies −10 Opinion -1 Score | 50% Levies −20 Opinion -2 Score |

#### Base Obligations

Clan government vassals have no obligations; assign to Tax Jurisdictions instead.

| Government | Levies | Taxes |
|---|---|---|
| Administrative | 30% | 75% |
| Celestial | 30% | 75% |
| Feudal | 10% | 25% |
| Herder | 0% | 0% |
| Ritsuryō | 10% | 10% |
| Sōryō | 10% | 25% |
| Mandala | 25% | 25% |
| Meritocratic | 30% | 75% |
| Nomad | 10% | 25% |
| Republic | 10% | 20% |
| Theocratic | 10% | 10% |
| Tribal | 0% | 0% |
| Wanua | 0% | 0% |

### Factions

Factions are organized vassal groups united against liege for common purpose. Unsolved factions grow until delivering ultimatums. Members unlock interactions to force joins (500 Influence or Strong Hook, 10-year lock). Factions track military power (faction vs liege+non-members ratio) and discontent. >80% power raises discontent; <80% lowers it. Ultimatums deliver at 100% discontent or after unjust imprisonment. Player-led factions send anytime. Acceptance: -20 Dread/Legitimacy. Refusal: civil war.

Vassals cannot join/create factions if landless, underage, Ceremonial Monarch, liege has Strong Hook/alliance/truce, or 80+ Opinion. Terrified vassals cannot join unless discontent rising. Can force with Hook. AI vassals cannot start/join if friends/lovers. Bureaucratic governments can only create faction if King+. Ritsuryō can only if house head with 50+ Cohesion bloc.

#### Civil Wars

Refused ultimatums trigger civil wars. Faction members stop providing taxes/levies; liege loses imprisonment powers. All factions turn hostile to liege and non-joining vassals (focus liege). All-dead factions: white peace if liege negative warscore, liege victory if positive.

White peace results: liege gains imprisonment cause on faction members.
Faction victory: enforce ultimatum.
Liege victory: imprison all members, gain +20 Dread, allow title revocation without tyranny. Popular opinion factions grant +20 opinion for 10 years per county.

#### Vassal Factions

Manually created by vassals. Require military power discontent. AI restrictions: first 10 years Emperor, 5 years King, 1 year Duke-. Creation/join likelihood depends on Realm Stability rule.

| Type | Ultimatum | Requirements |
|---|---|---|
| Liberty | Lower crown authority −200 Prestige (Meritocratic: change to Meritocratic Regency, create titular Kingdom) | Not lowest authority |
| Independence | All independent −150 Prestige | Independent Not Confederation member Not councilor in China |
| Dissolution | Primary title destroyed −150 Prestige (Emperor: also Kingdoms destroyed) | Independent Not Theocracy Not Muslim Dar al-Islam (not bureaucratic, not Ceremonial Monarchy) |
| Claimant | Claimant gains title +weak hook on claimant | Realm has claimant Not Ceremonial Monarchy |
| Imperial Policy | Leader chooses Imperial Policy −200 Prestige | Has Imperial Policy law Not Ceremonial Monarch |
| Rebellion | All independent −Fame level | Hegemony of China Yamen Grievance Drum upgraded |

Ceremonial Monarchy realms unlock 3 additional factions (AI restricted first 10 years; require 75 Cohesion for blocs):

| Type | Ultimatum | Requirements |
|---|---|---|
| Install Ruling Regent | Faction leader replaces liege −500 Prestige | Same government Doctrine allows Not Ceremonial Monarch |
| Ceremonial Claimant | Leader replaces liege, claimant replaces Ceremonial Monarch −500 Prestige | Has claimant Not Ceremonial/Liege Ceremonial |
| Restore Ceremonial Monarch | Ceremonial Monarch replaces liege −500 Prestige | Service house aspiration Not Ceremonial/Liege Ceremonial |

#### Popular Factions

Cannot be created/joined by vassals; auto-create from negative domain Popular Opinion (threshold: Realm Stability rule). Military power: member levies vs domain levies. Discontent doubles if Conditional Join or Dynastic Cycle Expansion/Tension/Conquest era. Siege captures kill instead of imprison. Civil wars end if leader dies.

| Type | Ultimatum | County requirements | Military power needed |
|---|---|---|---|
| Populists | Convert to faith/culture or independence −Fame | Different faith/culture 5 years passed (not Nomadic Settlement) | Yes |
| Peasant Rabble | −75 Control −50% Control growth +50 Popular opinion 10 years | Not Nomadic Settlement | No |
| Nomads | Form independent Nomadic realm −Fame | Has Nomadic Settlement/Herder Pens | No |

## Tributaries

Most independent subject type. Tributaries pay tribute in exchange for truce with suzerain (higher/equal rank). Nomadic/Celestial/Mandala governments can demand tributaries regardless of authority. Others need level 2 authority and war. Independent rulers always offer to become tributaries if suzerain allows.

Truce created. After expiry, tributary becomes independent (-75 Prestige -100 Opinion). Hegemons require initial tribute payment; thereafter regular payments expected.

All tributaries except Herder have contracts (changeable once per character). Herders give 20% Herd instead.

### Tributary Types and Contracts

| Type | Tribute options | None | Low | Medium | High | Extortionate | Truce | Suzerain | Inherited |
|---|---|---|---|---|---|---|---|---|---|
| Hegemonic | Taxes Prestige | 0% 0 Opinion +0.1 Legitimacy | 6%/-10 Opinion/+0.2 Legitimacy; 10% Prestige | 9%/-15 Opinion/+0.3; 15% Prestige | 18%/-30 Opinion/+0.5; 30% Prestige |  | 25y | Hegemony | Yes |
| Subjugated | Taxes Prestige | 0% +20 Opinion; 0% 0 Opinion | 15% +10 Opinion; 10% -10 Opinion | 30% -10 Opinion; 25% -25 Opinion |  |  | 15y | Tribal Feudal Clan Admin | No |
| Settled | Taxes Prestige Levies | 0% 0 Opinion (all) | 25%/-10; 10%/-10; 25%/-10 | 50%/-30; 25%/-25; 50%/-30 |  |  | 5y | Nomadic | Yes |
| Nomadic | Herd Prestige | 0% 0 Opinion (all) | 5%/-5; 15%/-10 | 10%/-10; 30%/-25 | 25%/-25; N/A | 40%/-35 | 5y | Nomadic | Yes |
| Mandala | Taxes Levies Piety | 0% +5; 0% 0; 5% +5 Opinion | 2.5% 0; 15% -5; 10% -5 | 10% -5; 30% -10; 15% -20 | 15% -20; 45% -25; N/A | 25% -30; 60% -35 | 5y | Mandala | Yes |
| Celestial | Taxes Prestige | 0% 0 Opinion +0.1 Legitimacy | 5%/-10 Opinion/+0.2; 5%/-10 Opinion/+0.2 | 10%/-15/+0.3; 10%/-15/+0.3 | 25%/-30/+0.5; 25%/-30/+0.5 |  | 25y | Celestial | Yes |
| Wanua | Taxes Prestige Barter Goods | 0% 0 Opinion (all) | 25%/-15; 10%/-15; 10%/-15 | 50%/-35; 25%/-30; 15%/-30 |  |  | 5y | Wanua | Yes |
| Steppe | Taxes Prestige | 0% 0 Opinion (all) | 25%/-10; 15%/-10 | 50%/-30; 30%/-25 |  |  | 5y | Meritocratic Khanate | Yes |

All tributaries except China can add:
- **Suzerain Guarantee**: Tributary calls suzerain to defensive wars +25 Opinion
- **Tributary War Support**: Tributary joins suzerain's wars −25 Opinion (requires Obedient or Blood Brother)

Tributaries have yearly stop-paying chance (military strength dependent). Suzerain can let them go independent or war.

### Pay Tribute

Tributaries use Pay Tribute decision to travel suzerain's capital. Tribute options: Gold, Treasury, Herd (Nomadic), unequipped Artifact, Concubine (if suzerain has tenet/tradition), Eunuch (if suzerain culture has traditions). Tributes give:

- 100 Legitimacy
- Random artifact (Illustrious only if best friends)
- +10% Tax +20% Development modifier (10 years) in realm capital
- Innovation (if culture difference and suzerain has innovation tributary lacks)
- Monk courtier (Mandala suzerain, unreformed tributary, different faith)
- Treasury (Hegemon of China; converts to Gold if tributary lacks Treasury)

Skill challenge available to choose gift (+5 Stress if failed).

Hegemons can demand tribute payment. Refusal: −50 Legitimacy.

### Hegemonic Tributaries

Independent rulers unlock Pay Tribute on Hegemons (required to become tributary). Tracks Subject Standing/Imperial Grace (0-100), visible in contract. Contracts changeable every 5 years. Request requires 20+ Subject Standing; decreases cost 10 per level. New tributaries start at 25. Pay Tribute grants 5-15 Standing (failed challenge) or 20-30 (succeeded). Decreases 1/year (doubled Expansion, tripled Tension/Conquest for China). AI hegemonies more likely to demand if Standing low.

#### China Tributaries

Can receive Seals of Investiture artifacts (70 Standing Count, 50 Duke, 30 King+). Costs 500 Treasury/Gold, grants +50 Legitimacy. Refusal: -50 Legitimacy -50 Opinion Hegemon. Seals unlock:

- **Family Access**: +Marriage Acceptance with suzerain dynasty, removes culture penalties
- **Market Access**: up to +50% Development Growth in realm capital
- **Palace Access**: Dynastic Cycle participant, grants Movement Power

## Lessees

Clergy subjects owning baronies (still part of holder's realm). Holdings provide levies/taxes to lessee (not domain limit). Character with only leased titles is unlanded. Can also be vassal if County+.

Holy order leases can be revoked (-500 Piety -40 Order Grandmaster Opinion -20 Head of Faith Opinion; destroys order if last lease revoked).

### Realm Priests

Theocratic faiths lease temples to Realm Priest councilor. Provides taxes/levies based on Opinion: 0 opinion minimum (nothing), 50 opinion maximum (50% taxes 100% levies). Vassal realm priests provide their liege's realm priest 25% taxes 15% levies (skip different religions). Independent realm priests pay 15% taxes 25% levies to Spiritual Head of Faith.

With 50+ opinion, each Stewardship point grants 1% extra taxes; each Martial point grants 2% extra levies from temple holdings.
