---
title: Schemes
category: intrigue-and-diplomacy
tags: [intrigue, personal schemes, hostile schemes, political schemes, agents]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Schemes]
---

Any character can run one scheme of each type simultaneously. Schemes can be canceled anytime, and various events may occur during execution. Character traits and statuses influence scheme values—a hideous character suffers penalties when seducing others, while higher-ranked characters are harder to target.

## Scheme mechanics

Each scheme tracks two core values:

- **Success Chance** grows over time and determines execution likelihood.
- **Phase Length** controls progression speed. For personal schemes, it determines completion; for hostile and political schemes, it controls advantage gain speed.

Hostile and political schemes have four additional values:

- **Potential** sets maximum success chance (capped at 95%, except contract schemes). Schemer skills contribute up to 30%, with agents providing the rest.
- **Secrecy** reduces discovery chance. Detection odds equal missing secrecy; breach gains occur monthly at one-tenth the missing secrecy rate. Secrecy is inactive during Grace (6 months normally, 10 with Court of Shadows perk).
- **Breaches** reduce success chance; reaching 5 causes automatic failure.
- **Advantage** executes schemes or entices agents. Requires 5 minimum to execute, or 10/15/20 for +5%/+10%/+20% success bonus (cannot exceed maximum). A schemer gains 1 advantage per 5 intrigue above 15.

## Hostile schemes

Hostile schemes use agents and secrecy. Failed secrecy grants the target an imprisonment reason against the schemer. Cannot target the schemer's own children unless they have Sadistic trait. War reduces Murder schemes by -50 success chance and Abduction by -500.

| Scheme | Skill | Max secrecy | Success effect | Requirements | Stress gain |
|---|---|---|---|---|---|
| Murder | Intrigue | 95% | Target is killed | None | +40 Honest +40 Just +80 Compassionate |
| Abduct | Intrigue | 85% | Target imprisoned | Kidnapper perk | +20 Honest +20 Just +40 Compassionate |
| Fabricate Hook | Intrigue | 95% | Gain hook on target | Truth is Relative perk or Vengeful trait vs Rival | |
| Claim Throne | Learning | 95% | Gain pressed claim on liege's primary title | Meritocracy perk Landed | |
| Steal Artifact | Intrigue | 95% | Gain artifact | Artifact claim | -30 Vengeful -15 Just +20 Honest |
| Overthrow Regent | Intrigue | 85% | Become new regent | Target is regent of same liege | |
| Siphon Treasury | Intrigue | 95% | Convert treasury to gold | Treasury | +40 Content |
| Seize Realm | Intrigue | 95% | Take target's titles | (Roads to Power) Adventurer government Illustrious fame Target is independent ruler | +40 Honest +40 Just +80 Compassionate |
| Steal Herd | Intrigue | 95% | Take herd from target | (Khans of the Steppe) Nomadic government Target has herd At war with target | +20 Compassionate +20 Content +20 Craven +20 Honest |
| Disbelieve Mandala | Intrigue | 95% | Target loses legitimacy and piety | Aspect of Trickery level 3 Mandala government Target is house head | |

## Personal schemes

Personal schemes lack secrecy and agents. Failure prevents reuse on the same character and may cause penalties.

| Scheme | Success effect | Failure effect | Requirements |
|---|---|---|---|
| Sway | 95% +25 opinion, 5% +30 opinion | 2% -10 opinion, 2% -10 opinion and target gains +1 Intrigue +8 Hostile Scheme Resistance for 5 years | |
| Learn Language | Schemer learns target's language | Can lose half progress for 35 stress; Diplomat trait grants +25 opinion | Target's language unknown |
| Seduce | +20 opinion, pregnancy chances, +20 opinion with opposite gender, lover or compatible sexuality secret | 40% -10 opinion, 20% gain Adulterer/Fornicator/Incestuous/Sodomite, 20% -10 opinion and trait loss | Compatible sexuality |
| Romance | Target becomes soulmate | 50% if no lover: -10 opinion; 50% if lover: attempt target or rival's death | Both characters compatible sexuality |
| Befriend | Best friend (if friend), rival ended, faction leader disbanded, faction member leaves | -20 opinion, -15 if rival, +20 faction discontent if leader, -10 capital control if theocracy vassal, -150 prestige if liege, expose random secret if spouse | Befriend perk |
| Elope | Target joins court and marries schemer, divorces current spouse | 50% lovers secret exposed | Target is lover/soulmate Unlanded In different court |
| Convert to Witchcraft | Gain witch trait or secret, mutual discovery if either has witch secret | Liege discovers secret if both vassal | Witch trait or secret |
| Mentorship | +10 merit per rank above schemer, gain Confucian education or experience, choose commander trait | | Celestial government Ruler or courtier At peace |

## Political schemes

Only available between characters with Administrative, Celestial, Ritsuryō, Meritocratic, or Meritocratic Khanate government in same realm. No failure effects except stress; exception is Raid Estate. Vassal discovery makes liege consider them criminal unless remit obtained. Liege discovery makes them rivals with target.

| Scheme | Skill | Agents | Secrecy | Success effect | Requirements |
|---|---|---|---|---|---|
| Expand Power Base | Stewardship | Yes | No | Gain +10%/+20%/+30% investment capacity 10 years | |
| Promote | Diplomacy | Yes | No | Target gains Promoted modifier 10 years: +20 appointment succession score +30 acclamation succession score +10% house relations | |
| Slander | Diplomacy | Yes | Yes | Target gains Slandered modifier 10 years: -25 appointment -50 acclamation -5% governor efficiency -10% house relations 20% negative nickname | Target not liege |
| Challenge Status | Learning | Yes | Yes | Take influence equal to scheme success chance, target loses 5% powerful family rating | Target not ceremonial monarch |
| Raid Estate | Intrigue | Yes | Yes | Gain gold, house members killed/maimed/imprisoned, estate building destroyed, house gains Estate Raided modifier 5 years: -25% domain taxes +25 building time Considered crime | House head, target house head, target not ceremonial monarch Administrative or 800 movement power |
| Border Dispute | Diplomacy | Yes | No | Take target's selected county | Target neighbor, target not liege, no fixed border policy |
| Subsume Governorship | Diplomacy | Yes | No | Take target's selected duchy | Powerful/dominant family head, target neighbor, target not liege, no fixed border policy |
| Depose | Intrigue | Yes | Yes | Replace top liege, choose fate | Powerful/dominant family head Target emperor+ Meritocratic no negative physical traits, no merit rank 4+, Celestial no tension era |
| Ingratiate Family | Diplomacy | No | No | Gain +60 influence, house +5% influence 10 years, +30 opinion, friendship chance | Fine living or guest houses upgrade |
| Mentor in Governance | Stewardship | Yes | No | Gain +60 influence, +15 opinion, governor trait gain/experience | Private study or law library upgrade, no rival |
| Promote Movement Power | Diplomacy | Yes | No | Movement gains +100 personal power per merit rank | In dynastic cycle |
| Slander Movement Power | Diplomacy | Yes | No | Movement loses -100 personal power per merit rank | In dynastic cycle, target not same movement |
| Damage Legitimacy | Intrigue | No | Yes | Target loses 50 legitimacy | Target is liege, no celestial government |
| Foster Legitimacy | Intrigue | No | No | Target gains 100 legitimacy, 50-89% 50% weak hook, 90-100% 50% strong hook | Target is liege, no celestial government |
| Find Secrets | Intrigue | No | No | Choice of gold or treasury, discover secret if available | Imperial censor or minister of justice, target not liege |

## Mandala schemes

Available to Mandala rulers with Aspect of Trickery. Both schemes target same ruler once per 5 years, no secrecy. Intrigue-based.

**Leverage Contribution:** Only available during underfunded great project. Success: target funds random contribution, gains +15 opinion, friendship progress. Failure: schemer gains +20 stress, target gains -5 general opinion 10 years.

**Coerce Tributary:** Requires level 2+ Mandala Aspect; level 3 targets higher rank only. Success: target becomes tributary, gains +30 opinion. If already tributary, prior suzerain may lose tributary and prestige/legitimacy, pay piety and scaled gold, or war the tributary.

## Agents

Most hostile and political schemes support up to 5 agents—adult characters contributing to schemes. Only target's courtiers, guests, and direct vassals qualify; cannot be imprisoned or in other schemes. Each agent caps at +50 contribution. Scheming characters have discovery protection; agents do not.

Acceptance depends on agent's opinion of schemer, schemer's skills, target's title rank, and realm distance. Relationships boost (+100 best friend, +50 friend, +25 lover). Characters terrified of target refuse except via strong hook. Some events grant additional agent slots.

### Agent closeness bonuses

| Closeness | Success chance |
|---|---|
| Spouse | +30 |
| Guardian | +30 |
| Concubine | +20 |
| Close Family | +10 |
| Extended Family | +5 |

| Closeness (Realm) | Success chance |
|---|---|
| Diarch | +30 |
| Councilor | +10 |
| Powerful Vassal | +5 |
| Vassal | +2 |

| Closeness (Court Position) | Success chance |
|---|---|
| Personal Physician | +20 |
| Cup-Bearer | +20 |
| Food Taster | +20 |
| Bodyguard | +20 |
| Chief Eunuch | +20 |
| Lady-in-waiting | +5 |

| Closeness (Relation) | Success chance |
|---|---|
| Best Friend | +30 |
| Friend | +20 |
| Lover | +20 |
| Nemesis | +10 |
| Rival | +5 |

### Swaying agents

Enticements to recruit agents:

| Enticement | Bonus |
|---|---|
| Leverage 3 scheme advantages | +10 |
| Leverage 5 scheme advantages | +30 |
| Bribe | +10 (scales by rank, -50% with Guile legacy) |
| Hefty Bribe | +20 (scales by rank, -50% with Guile legacy) |
| Offer hook on yourself | +20 (~20 stress) |
| Use your hook on them | +100 |
| Offer prestige | +20 |
| Offer influence | +20 (Administrative only) |
| Grant council seat | ? (agent must be landed vassal) |
| Grant county they claim | ? (you must own it) |
| Offer piety | +20 (agent must be zealous) |

### Agent personality

Characters vary in willingness to scheme based on AI personality. Personality titles suggest traits; hidden values (boldness, compassion) matter more.

- Most characters (even generous ones) face -10 penalty for "nothing to gain" unless disliking target. Greedy characters suffer -35 penalty unless gaining title from death; they get +20 gold bribes instead of +10, removing the "nothing to gain" penalty.
- Low boldness incurs -10 penalty ("too dangerous"); cowardly characters face -100, stacking with intimidation.
- Compassionate characters (gracious, empaths) face -40 immoral penalty; scales to +10 for evil villains.
- Vengefulness grants +40 bonus against those who slighted character, even non-rivals.
- Religious characters (+10 to +25 vs astray faiths, doubled for hostile/evil) scheme more against different religions.

### Agent types

Quick reference for agent arrangements by scheme:

| Scheme | Balanced | Potential Focus | Phase Length Focus | Secrecy Focus |
|---|---|---|---|---|
| Murder | Assassin, Assassin, Infiltrator, Footpad, Alibi | Assassin, Assassin, Thug, Infiltrator, Alibi | Infiltrator, Infiltrator, Footpad, Assassin, Alibi | Alibi, Alibi, Lookout, Assassin, Infiltrator |
| Abduct | Thug, Muscle, Footpad, Infiltrator, Lookout | Thug, Thug, Muscle, Footpad, Lookout | Footpad, Footpad, Infiltrator, Thug, Lookout | Lookout, Lookout, Decoy, Thug, Footpad |
| Fabricate Hook | Outcast, Thief, Infiltrator, Footpad, Lookout | Outcast, Diplomat, Thief, Infiltrator, Lookout | Infiltrator, Footpad, Socialite, Outcast, Lookout | Lookout, Decoy, Justiciar, Outcast, Footpad |
| Steal Artifact | Thief, Thief, Infiltrator, Infiltrator, Lookout | Thief, Thief, Thug, Infiltrator, Lookout | Infiltrator, Infiltrator, Footpad, Thief, Lookout | Lookout, Alibi, Decoy, Thief, Infiltrator |

### Potential agents

Agents increasing scheme potential. Eunuch type requires Eunuch trait and court eunuchs/Byzantine/palace politics tradition. Devotee added by positive camp temperament events.

| Agent type | Skills | Trait bonuses | Trait penalties | Description |
|---|---|---|---|---|
| Alchemist | +0.75 Learning | +9 Ambitious, Novice Physician, Herbalist; +6 Wise; +3 Calm, Eccentric, Shrewd | -9 Blind, Craven; -6 Impatient; -3 Content, Cynical | Understanding creation's forces |
| Ambusher | +0.75 Intrigue, +0.25 Martial | +9 Hunter, Schemer, Traveler; +6 Callous, Deceitful; +3 Cynical, Patient, Sadistic | -9 Just, Loyal; -6 Compassionate, Forgiving, Honest; -3 Fickle, Impatient | Hit first, hard, unexpectedly |
| Assassin | +0.75 Prowess, +0.25 Intrigue | +9 Vengeful (Rivals), Callous, Patient, Sadistic; +6 Brave, Deceitful; +3 Arbitrary | -9 Forgiving (Rivals), Compassionate, Impatient; -6 Craven, Honest; -3 Just | Knife, poison, pitchfork |
| Bailiff | +0.75 Learning, +0.25 Diplomacy | +9 Administrator, Overseer; +6 Just, Vengeful; +3 Honest, Stubborn | -9 Content, Shy; -6 Compassionate, Fickle; -3 Forgiving, Trusting | Enforce what's written |
| Bodyguard | +0.75 Prowess, +0.25 Martial | +9 Herculean/Amazonian, Strong; +6 Shieldmaiden/Shieldswain, Berserker, Robust; +3 Hale, Humble, Vengeful, Wrathful | -9 Feeble, Weak, Craven; -6 Frail; -3 Delicate, Forgiving, Temperate | Sword in arm's reach |
| Bookkeeper | +0.75 Learning, +0.25 Stewardship | +9 Scholar, Theologian; +6 Eccentric, Humble; +3 Diligent, Patient, Shy | -9 Arbitrary, Lazy; -6 Impatient; -3 Arrogant, Deceitful | Sums match perfectly |
| Cleric | +0.75 Diplomacy, +0.25 Learning | +9 Zealous; +6 Diligent, Humble; +3 Honest | -9 Cynical; -6 Arrogant, Lazy; -3 Deceitful | Faith demands fire |
| Comrade-in-Arms | +0.5 Diplomacy, +0.5 Intrigue | +9 Gregarious, Lustful; +6 Brave, Compassionate, Deceitful; +3 Trusting | -9 Chaste, Shy; -6 Callous, Craven, Honest, Sadistic; -3 Paranoid | Private talk in crowd |
| Diplomat | +0.75 Diplomacy, +0.25 Intrigue | +9 Calm, Deceitful, Gregarious; +6 Arbitrary, Arrogant, Patient; +3 Ambitious | -9 Honest, Shy, Wrathful; -6 Humble, Impatient, Just; -3 Content | Delicate touch, whispered words |
| Draughtsman | +0.75 Learning, +0.25 Stewardship | +9 Architect; +6 Administrator, Journaller; +3 Ambitious, Diligent, Scholar | -9 Content, Lazy; -6 Fickle, Impatient; -3 Forgiving, Generous | Engineer ideas to reality |
| Lookout | +0.75 Intrigue, +0.25 Martial | +9 Diligent, Paranoid, Patient; +3 Brave | -9 Impatient, Lazy; -6 Trusting; -3 Craven | Eyes watch hands |
| Muscle | +1 Prowess | +9 Herculean/Amazonian, Athletic, Giant, Strong; +6 Shieldmaiden/Shieldswain, Berserker, Robust, Varangian; +3 Brave, Hale | -9 Feeble, Weak; -6 Compassionate, Craven, Frail; -3 Delicate, Forgiving, Just | More brawls than brains |
| Musician | +0.75 Diplomacy, +0.25 Learning | +9 Eccentric, Stubborn; +6 Content, Diligent, Lazy; +3 Gregarious, Patient, Shy | -9 Fickle; -6 Ambitious, Impatient | Life without music is bereft |
| Outcast | +0.75 Intrigue, +0.25 Diplomacy | +9 Humble, Shy; +6 Craven, Patient, Schemer; +3 Deceitful, Eccentric, Paranoid, Shrewd | -9 Ambitious, Gregarious; -6 Fickle, Honest; -3 Trusting | Wretch in shadows |
| Outrider | +0.75 Martial, +0.25 Diplomacy | +9 Hunter, Traveler; +6 Forder; +3 Diligent, Patient | -9 Blind; -6 Craven, Fickle; -3 Impatient, Stubborn | Mobility key |
| Physic | +0.75 Learning | +9 Novice Physician, Whole of Body; +6 Herbalist, Wise; +3 Calm, Patient, Shrewd | -9 Blind, Drunkard; -6 Impatient, Wrathful; -3 Deceitful, Sadistic | Strong stomach |
| Poet | +0.5 Diplomacy, +0.25 Intrigue, +0.25 Learning | +9 Brave, Gregarious; +6 Arrogant, Content, Lazy; +3 Compassionate, Sadistic | -9 Craven, Shy; -6 Ambitious, Diligent, Humble; -3 Callous | Unmitigated talent |
| Poisoner | +0.75 Prowess, +0.25 Intrigue | +9 Vengeful (Rivals), Callous, Lazy, Patient, Sadistic; +6 Deceitful, Diligent, Herbalist, Novice Physician; +3 Arbitrary, Witch | -9 Forgiving (Rivals), Compassionate, Impatient; -6 Craven, Honest; -3 Just | Right herb mix |
| Scout | +0.75 Intrigue, +0.25 Martial | +9 Hunter, Traveler; +6 Forder; +3 Diligent, Patient | -9 Blind; -6 Craven, Fickle; -3 Impatient, Stubborn | Know what's ahead |
| Scribe | +0.75 Learning, +0.25 Stewardship | +9 Humble; +6 Diligent, Patient, Shy; +3 Calm, Content | -9 Arrogant; -6 Gregarious, Impatient, Lazy; -3 Ambitious, Wrathful | Confident letters, humble instructions |
| Shill | +0.75 Intrigue, +0.25 Diplomacy | +9 Deceitful, Gregarious; +6 Arbitrary; +3 Brave | -9 Honest, Shy; -6 Just; -3 Craven | Friendly stranger in crowd |
| Smith | +0.75 Stewardship, +0.25 Prowess | +9 Architect; +6 Ambitious; +3 Calm, Diligent, Strong | -9 Lazy, Weak; -6 Impatient, Temperate; -3 Content, Fickle | Art wrought |
| Theologian | +0.75 Learning, +0.25 Diplomacy | +9 Just, Stubborn, Zealous; +6 Calm, Diligent, Wrathful; +3 Eccentric | -9 Arbitrary, Cynical, Fickle; -6 Lazy | Rhetoric and resolve |
| Thief | +0.75 Intrigue, +0.25 Prowess | +9 Arbitrary, Patient; +6 Deceitful, Paranoid; +3 Ambitious, Arrogant | -9 Impatient, Just; -6 Honest, Trusting; -3 Content, Humble | Violence marks amateur |
| Thug | +0.75 Prowess, +0.25 Intrigue | +9 Impatient, Wrathful; +6 Callous, Sadistic; +3 Arrogant, Gregarious | -9 Calm, Patient; -6 Compassionate; -3 Craven, Humble, Shy | Cosh skull |
| Tumbler | +0.75 Prowess, +0.25 Diplomacy | +9 Brave; +6 Calm; +3 Temperate | -9 Craven; -6 Wrathful; -3 Gluttonous | Window or wall |
| Tutor | +0.75 Learning, +0.25 Stewardship | +9 Diligent, Patient; +6 Compassionate, Humble; +3 Calm, Eccentric, Gregarious | -9 Impatient, Sadistic; -6 Arrogant, Callous, Lazy; -3 Wrathful | Adapts to student |
| Wolf Hunter | +0.75 Prowess, +0.25 Martial | +9 Brave, Eccentric, Stubborn; +6 Compassionate; +3 Diligent | -9 Craven; -6 Callous, Sadistic; -3 Lazy | Romance needs danger |
| Wraggler | +0.75 Diplomacy, +0.25 Intrigue | +9 Diplomat, Gregarious; +6 Ambitious, Arrogant; +3 Eccentric | -9 Content, Forgiving, Shy; -6 Humble, Trusting; -3 Temperate | Calming and intimidating |
| Eunuch | +0.75 Intrigue, +0.25 Learning | +9 Disloyal (Depose), Callous, Deceitful, Patient; +6 Diligent, Herbalist, Novice Physician; +3 Arbitrary | -9 Loyal (Depose), Compassionate, Honest, Impatient, Lazy; -6 Craven; -3 Just | Silent keeper of secrets |
| Devotee | +0.75 Intrigue, +0.25 Diplomacy | +9 Eccentric, Gregarious; +6 Drunkard; +3 Arrogant | -9 Shy; -6 Callous; -3 Cynical | Devoted to leader |

### Administrative agents

Administrative government only:

| Agent type | Skills | Trait bonuses | Trait penalties | Requirements |
|---|---|---|---|---|
| Sycophant | +0.75 Diplomacy, +0.25 Intrigue | +9 Deceitful, Stubborn; +6 Greedy; +3 Arbitrary, Arrogant, Diligent | -9 Honest, Humble; -6 Patient; -3 Just | Compliment powerful |
| Intermediary | +0.75 Diplomacy, +0.25 Intrigue | +9 Calm, Deceitful, Gregarious; +6 Ambitious, Arbitrary, Arrogant, Patient | -9 Honest, Shy, Wrathful; -6 Humble, Impatient, Just; -3 Content | Governor or house head |
| Proponent | +0.75 Diplomacy, +0.25 Intrigue | +9 Calm, Deceitful, Gregarious; +6 Ambitious, Arbitrary, Arrogant, Patient | -9 Honest, Shy, Wrathful; -6 Humble, Impatient, Just; -3 Content | Governor or house head |

### Phase length agents

Agents reducing scheme phase length:

| Agent type | Skills | Trait bonuses | Trait penalties | Description |
|---|---|---|---|---|
| Drillmaster | +0.75 Martial | +9 Diligent, Patient; +6 Athletic, Shrewd, Stubborn; +3 Ambitious, Organizer | -9 Content, Lazy; -6 Impatient; -3 Fickle, Wrathful | Drill at best, fight at worst |
| Footpad | +0.5 Intrigue, +0.5 Prowess | +9 Deceitful, Patient; +6 Calm; +3 Shy | -9 Honest, Impatient; -6 Wrathful | Knife in back alley |
| Gabbler | +0.5 Diplomacy, +0.5 Intrigue | +9 Eccentric, Fickle, Gregarious; +6 Arrogant, Lazy; +3 Brave | -9 Shy, Stubborn; -6 Diligent, Humble; -3 Craven | Hour without saying thing |
| Herald | +0.75 Diplomacy, +0.25 Stewardship | +9 Arrogant, Gregarious; +6 Diligent; +3 Trusting, Patient | -9 Humble, Shy; -6 Lazy; -3 Paranoid | Loud, emphatic, bold |
| Infiltrator | +0.5 Intrigue, +0.5 Diplomacy | +9 Deceitful, Gregarious; +6 Diligent; +3 Patient | -9 Honest, Shy; -6 Lazy; -3 Impatient | Unlocked latch, hungover guard |
| Justiciar | +0.75 Learning, +0.25 Diplomacy | +9 Diligent, Honest, Just; +6 Patient; +3 Paranoid | -9 Arbitrary, Deceitful, Diligent; -6 Impatient; -3 Trusting | Law and fairness |
| Planner | +0.75 Learning, +0.25 Stewardship | +9 Architect, Paranoid; +6 Administrator, Diligent; +3 Gregarious, Journaller, Scholar | -9 Content, Lazy, Profligate; -6 Fickle, Impatient; -3 Forgiving, Generous | Expert improvises |
| Socialite | +0.5 Diplomacy, +0.25 Intrigue, +0.25 Learning | +9 Ambitious, Gregarious; +6 Arrogant, Compassionate, Lazy, Sadistic; +3 Fickle | -9 Content, Shy; -6 Callous, Humble; -3 Diligent | Toast to good friend |
| Supplier | +0.75 Stewardship, +0.25 Diplomacy | +9 Avaricious, Overseer; +6 Logistician, Organizer, Schemer; +3 Deceitful, Generous, Gregarious, Shrewd | -9 Profligate, Shy, Stubborn; -6 Fickle, Impatient; -3 Forgiving, Greedy | Connections and timing |
| Tracker | +0.75 Martial, +0.25 Intrigue | +9 Hunter, Traveler; +3 Diligent, Patient | -9 Blind, Impatient, Lazy; -6 Arbitrary, Arrogant; -3 Fickle | Mud still damp |
| Bureaucrat (Duke+) | +0.75 Learning, +0.25 Stewardship | +9 Architect, Paranoid; +6 Administrator, Diligent; +3 Gregarious, Journaller, Scholar | -9 Content, Lazy, Profligate; -6 Fickle, Impatient; -3 Forgiving, Generous | Process and filing |

### Secrecy agents

Agents increasing scheme secrecy:

| Agent type | Skills | Trait bonuses | Trait penalties | Description |
|---|---|---|---|---|
| Decoy | +0.75 Intrigue, +0.25 Diplomacy | +9 Eccentric, Gregarious; +6 Brave, Diligent, Paranoid | -9 Lazy; -6 Content, Trusting; -3 Craven | Spilled goblet |
| Justiciar | +0.75 Learning, +0.25 Diplomacy | +9 Diligent, Honest, Just; +6 Patient; +3 Paranoid | -9 Arbitrary, Deceitful, Diligent; -6 Impatient; -3 Trusting | Law and fairness |
| Courtesan | +0.75 Diplomacy, +0.25 Intrigue | +9 Herculean/Amazonian, Beautiful, Deceitful, Lustful; +6 Handsome/Pretty, Ambitious, Gregarious, Robust; +3 Comely, Compassionate, Hale, Patient | -9 Chaste, Feeble, Hideous, Honest; -6 Callous, Frail, Ugly; -3 Delicate, Homely, Shy | Spill secrets to beautiful | Sexual orientation matches target |
| Amanuensis | +0.75 Learning, +0.25 Stewardship | +9 Architect, Paranoid; +6 Administrator, Diligent; +3 Gregarious, Journaller, Scholar | -9 Content, Lazy, Profligate; -6 Fickle, Impatient; -3 Forgiving, Generous | Always ignored corner | Courtier |
| Alibi | +0.75 Diplomacy, +0.25 Learning | +9 Honest, Just, Loyal; +6 Confider, Gregarious, Humble; +3 Content | -9 Arbitrary, Deceitful, Disloyal; -6 Arrogant, Contrite, Shy; -3 Ambitious | With me all evening | Ruler/councilor/target family |
| Eunuch | +0.75 Intrigue, +0.25 Learning | +9 Disloyal (Depose), Callous, Deceitful, Patient; +6 Diligent, Herbalist, Novice Physician; +3 Arbitrary | -9 Loyal (Depose), Compassionate, Honest, Impatient, Lazy; -6 Craven; -3 Just | Silent keeper of secrets | Eunuch trait; court eunuchs/Byzantine/palace politics tradition |

## Countermeasure focus

Characters choose countermeasure focus for bonuses against schemes with penalties. Three tiers available. Tier 2 unlocked by paranoid trait or palace politics tradition. Tier 3 requires specific traditions, tenets, or traits. Domiciles unlock some tiers.

Most countermeasures affect all court members; "Withdraw from View" affects only the ruler.

| Countermeasure | Tier 1 | Tier 2 | Tier 3 | T3 Requirements |
|---|---|---|---|---|
| Bounties for Whispers | -15% enemy secrecy, -10% gold, -20% prestige | -15% enemy secrecy, -7% gold, -15% prestige | -35% enemy secrecy, -2% gold, -5% prestige | Astute Diplomats or Sacred Lies |
| Arbitrary Arrests | -25% enemy secrecy, +30% tyranny, -30 opinion, -40 popular opinion | -25% enemy secrecy, +20% tyranny, -20 opinion, -30 popular opinion | -35% enemy secrecy, +10% tyranny, -20 opinion, -30 popular opinion | Life is just a Joke |
| Strengthen Sentries | -100% personal scheme, +15% hostile scheme, -10 opinion, -30 vassal opinion | -100% personal scheme, +15% hostile scheme, -30 vassal opinion | -100% personal scheme, +15% hostile scheme, -20 vassal opinion | Isolationist |
| Redouble Guards | -100% hostile scheme, +15% personal scheme, -10 opinion, -30 vassal opinion, +20% stress | -100% hostile scheme, +15% personal scheme, -20 vassal opinion, +15% stress | -100% hostile scheme, +15% personal scheme, -20 vassal opinion, +10% stress | Isolationist |
| Withdraw from View | -100% hostile/personal scheme, +25% claim throne/hook chance, -30 opinion, +30% stress | -100% hostile/personal scheme, +25% claim throne/hook chance, -30 opinion, +20% stress | -125% hostile/personal scheme, +25% claim throne/hook chance, -20 opinion, +10% stress | Pastoral Isolation/Reclusive/Shy |
| Bribe Officials | -50% political scheme, -8% income/influence (T1) | -100% political scheme, -6% income/influence (T2) | -150% political scheme, -4% income/influence (T3) | Palace Politics + Servant's Quarters level 4 |

Administrative, Celestial, Meritocratic, Meritocratic Khanate, and Ritsuryō rulers have Bribe Officials (T2 unlocked by Palace Politics or Servant's Quarters level 4; T3 by both).
