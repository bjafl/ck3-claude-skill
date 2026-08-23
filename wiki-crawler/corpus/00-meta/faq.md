---
title: FAQ
category: meta
tags: [faq, meta, developer-commentary, pre-launch, mechanics-overview]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/FAQ]
---

Community Q&A with Paradox developers, originally published in 2020 before launch. Answers
describe development-time intent for a pre-launch build, not necessarily the shipped or
current (1.19) game — several systems discussed here (schemes, cultural innovations,
governments) were substantially reworked in later patches and DLC. Marketing and pre-order
content has been dropped; each section below has been checked against current CK3 knowledge
and flagged or trimmed where it looks outdated. Cross-check against the dedicated mechanic
files in this corpus where they overlap.

## Dynasties, Houses

Barony vassals can't be transferred out of their county or inherited from a county you don't
hold — an orphaned barony reverts to whoever holds the county instead (baronies are always
part of a county), though leasing a barony to another ruler or a Holy Order gives them the
holding and its income without it leaving your realm. Barons remain full characters, just
de-emphasized. Legacies can be picked from any unlocked track, but late picks in a track are
much stronger than early ones, so committing to one track before branching out pays off. AI
dynasties actively found houses and branch out. You choose your own house name and motto.
Cadet-branch coats of arms are partially derived from the parent house's arms, though not all
historical dynastic heraldry made it in. A dynasty head can lose that status if a rival house
becomes more powerful (e.g., a younger brother founding a more powerful house); a marriage
between two cadet branches does not spin off a new dynasty — children take the primary
partner's dynasty. "Dynast" was renamed "Dynasty Head" for clarity, and house-head power was
stated to be driven mainly by military strength (this specific weighting may have changed
since). See [Rulers & Dynasties](../07-rulers-and-dynasties/).

## Medieval Map

Terrain can't be altered by event/script effects. Major rivers (e.g. the Thames) can only be
crossed at designated fords, and empty baronies exist for later construction, much like unused
holding slots in CK2. The map is flat, roughly CK2-sized but without China, and extends further
than CK2 to include all of Tibet, sub-Saharan Africa to the Nigerian coast, more of Mongolia,
and more of Bengal, using a bespoke in-house projection rather than a standard one. It ends just
west of the Canary Islands, reaches almost to the equator down Africa's west coast, and goes as
far east as Burma. Only county names appear at zoom (three zoom levels; no barony-name display),
and the game is fully moddable at the map level with built-in tools. Terrain mapmode shows a
glowing border gradient at zoom. Mountain chokepoints don't block movement outright but heavily
funnel it, letting a defender predict enemy paths and get a significant combat bonus fighting in
mountains — further boosted by defensive buildings.

## War

Cultural Men-at-Arms replace CK2's retinue bonuses: steppe cultures get Horse Archers, Greeks
get Cataphracts, etc. MAA are distinct from levies, aren't raised constantly, and are costly (not
prohibitively) to swap. There's no EU4-style zone of control; hostile-territory attrition acts as
a "soft" deterrent instead. Occupying every fortified holding in a county auto-captures the rest
of it. Female knights/commanders are allowed wherever the culture/faith historically permitted
shieldmaidens (e.g. Norse). Knighthood isn't a granted title — it defaults to your highest-Prowess
characters (adjustable manually) and knights fight directly in battle, dealing and taking real
damage, and can be wounded, captured, or killed. Rushing into enemy territory causes heavy
attrition, which the AI is aware of and avoids, preferring to siege its way toward its war goal.
Battle events are influenced by commander/knight presence; an overwhelming victory raises capture
odds, and capturing the enemy ruler outright wins the war. Shattered retreat exists. Only knights
and commanders — not ordinary characters — fight in battles, and knight counts are capped by tier
and other modifiers. There was no naval combat planned at launch and none has been added since
(fleets exist only for transport). Peace terms are still limited to the war's original casus
belli, as in CK2. Army quality reflects the amount and quality of Men-at-Arms and Knights, not
just the levy-to-MAA ratio — a few excellent Knights can raise it more than many mediocre ones.
Embarkation cost is flat regardless of destination, but troop maintenance rises while at sea. See
[Warfare](../05-warfare/).

## Development, Buildings

Duchy-capital buildings are tied to one specific barony (e.g. Essex's duchy buildings must be
built in London). CK3's special/"Great Work"-style buildings are simpler than CK2's and only
represent real historical buildings. Tribal and never-built holdings make up the minority of
holding types; counties can't gain holding slots beyond what exists at map start, though many
(especially at the 867 start) begin with empty ones to fill in. County development can be
reduced by raiding/devastation. There are no unique cultural buildings — what you can build in a
barony is driven by terrain instead (Farmland gives higher economic output; Desert favors hardier
warriors). Domain economy comes down to buildings, development, control, and vassal taxes, all
abstracted into gold. Duchy Capital buildings are the mechanism for effects that touch every
county in a duchy at once (roads, irrigation, etc.).

## Schemes, Secrets, Hooks

> ⚠️ CK3's scheme/intrigue system went through a significant rework after launch (scheme phases,
> revised power/resistance math), so the specific numbers and behaviors described in these
> pre-launch answers may not match the current implementation. See
> [Intrigue & Diplomacy](../04-intrigue-and-diplomacy/) for current mechanics.

Seduction requires the target to be plausibly attracted to the seducer. Refusing a blackmail
demand exposes your secret instead. If one agent in a scheme is discovered, the others generally
stay hidden — the target just knows *someone* is scheming. A secret can eventually "get lost" if
everyone involved in it dies. Agent "closeness" (family, councillor status, etc.) increases the
Scheme Power they contribute. A scheme discovered before execution isn't automatically traced
back to you, but it does raise the odds you'll be caught executing it. You can't blackmail
someone over a secret you're also implicated in. Children can't run murder schemes. Sexuality is
modeled outside the trait system, with bisexual characters present. Murdering your own adult
children is possible only for Sadistic characters. Assassination success depends on multiple
factors, including your agents, not a flat coin flip. AI characters pursue comparatively
reasonable schemes (e.g. murdering their way up the succession, taking revenge on rivals) rather
than CK2-style impulsiveness.

## Council, Powerful Vassals, Spouse Councillor

A bishop serves as your religious councillor, collecting taxes from same-faith bishops beneath
you and from temple holdings in your own domain — but ecclesiastic characters can also
independently hold land and title in their own right, separate from that role. A high-opinion
spouse actively helps run the realm and can unlock unique opportunities; a spouse with the wrong
personality (given a low opinion of you) can instead work against you. If a character's parentage
is later called into question, they take diplomacy/prestige penalties but keep their claims — and
it's excellent blackmail material. A capable lowborn courtier or guest can be made Steward
regardless of birth, though your noble vassals won't like it. Council tasks like "convert county"
show a progress bar with occasional associated random events, rather than a flat yearly
percentage chance. The CK2 favor system was replaced by the more involved hooks system, alongside
dedicated vassal and succession laws.

## Characters & Portraits

A barbershop lets you customize hair, facial hair, clothes, and (to a limited degree) hair color.
High skill values (into the 20s) were still being balanced pre-launch. Personality is very hard to
change and never shifts from a random event — the main driver of change after childhood is a
stress-induced midlife crisis. Overall abstracted health is shown via a small heart icon (a
withered black heart signals serious illness), without ever giving an exact time of death.
Genetic traits are visible; recessive traits are hidden but can still be passed on. Event
animations reflect context (e.g. shock at a spouse's infidelity). The age of adulthood remains
16, but portraits now age gradually rather than jumping at hard boundaries. Mixed-heritage
children blend both parents' appearance with some randomness. Adoption was not planned for
release (and still isn't a CK3 mechanic). Clothing and headgear access scale with title rank and
are otherwise fully customizable in the barbershop. Family members without a close inheritance
claim can leave to become wanderers, and dynasty heads can formally Disinherit members. A
character's DNA/ethnicity is independent of and unaffected by later culture changes. See
[Character Mechanics](../01-character-mechanics/).

## Courts, Guests, and Wanderers

Wanderers exist specifically to reabsorb excess courtiers — new characters are generated mainly
when no wanderers are available, and some wanderers eventually die off if they find no place to
go. Families generally travel together unless separated by misfortune. Seven courtiers is only a
loose baseline: fewer courtiers draws more guests, and you can build a large court if you're
willing to give people a reason to stay. Wanderers mostly drift to adjacent realms, occasionally
"teleporting" further. You can invite specific people to court (they're more reluctant than in
CK2) or use hooks to compel them. Pressing a courtier's claim makes them your vassal directly.
Courtiers recruited without a strong tie tend to leave after roughly 3 years on average, longer
if they're a patient claimant or personally fond of you. Courtiers also appear as agents and
characters within events.

## Lifestyles

The lifestyle system (perks, perk trees, focuses, even whole lifestyles) is heavily moddable.
Some Legacies grant the whole dynasty bonus XP gain. You accumulate XP in a Lifestyle via your
active Focus, which you can always have set, and can freely switch (short cooldown) while
retaining every perk earned under a previous Focus. A handful of genetic traits (tiered
Intelligence) boost learning. Events are generally scoped to your active Lifestyle, though rare
cross-lifestyle perk progress is possible. There was no supernatural content planned for the base
game, though pursuing alchemy or witchcraft knowledge was teased as having "other uses."

> ⚠️ The base game indeed shipped without supernatural content, but this changed with the *Fate
> of Iberia* flavor pack, which introduced sorcery/witchcraft mechanics (requires Fate of Iberia).

Lifestyle events are designed to work across cultures/faiths rather than being faith-specific.
Education traits matter more in CK3 since they also boost XP gain and attributes; a full focus
tree was estimated at roughly 25 years without bonuses (a pre-launch figure that may have shifted
with later balancing). An unlanded heir accrues Lifestyle XP scaled to age/skill to spend once
landed. The Learning lifestyle affects custom-faith/heresy creation. Nomadic government does not
exist — realms that were nomadic in CK2 are Tribal in CK3, and that remains true today. Romance,
Elopement, and Seduction schemes vary significantly by the target's personality rather than
playing out the same way each time. The "about to die" alert is not a hardcoded lifespan, just a
probabilistic warning. Lifestyle traits unlock via the perk trees themselves rather than linear
events, giving a large pool of possible events instead of CK2's more linear progression. Children
lean toward the Lifestyle matching whatever education their guardian chose for them. Unlanded
rulers stop progressing their lifestyle until landed again. Hunting is available as a
non-gender-locked decision, mainly as a stress outlet. Long-lived (or modded-immortal) characters
can accumulate multiple lifestyle traits over one lifetime; immortality itself is not in vanilla
but is moddable. Anyone's lifestyle trees are inspectable. Nicknames can be overwritten by more
"significant" ones your reputation earns later (e.g. "Conqueror" outranks "the Drunkard").

## Seduction, Torture, and the Intrigue Perk Trees

A long-lived character with education matching their Lifestyle can typically fill 2–3 perk trees
over a lifetime. Seduction works regardless of whether the target's orientation matches your
gender, though lacking the relevant perk imposes a significant penalty; you can act against your
own orientation to seduce someone, but can't make others do the same. Consequences for getting
caught seducing someone (e.g. an heir's spouse) scale with how the target's faith views adultery.
Perks and points can be freely mixed across the Intrigue trees (Seducer, Torturer, etc.) — a
single Lifestyle perk unlock can be spent on any of its trees regardless of prior picks. Romantic
schemes require the target's orientation to match your gender, but success chance depends heavily
on personality. Higher tier gaps make seduction harder (a countess seducing an emperor is a much
tougher ask) but not impossible. Your own spouse can be seduced into becoming a lover or soulmate.

## Tutorial & Encyclopedia

The in-game Encyclopedia works fully offline. "Edge scrolling" pans the camera when the cursor
nears the window edge — useful to disable in windowed mode or multi-monitor setups.

## Governments, Vassal Management, Laws, and Raiding

Only a realm already hostile to a raiding army can intercept and steal its loot — you can't do
this to a raider who hasn't touched your land (requires Northern Lords). Crushing raiders who've
already looted one of your vassals lets *you* claim that gold, leaving the vassal with a "Recently
Looted" penalty rather than a direct loss — worse for them than for you. You can't build directly
from the Domain tab, but clicking a holding there opens its holding view. Governments are
moddable, though Republics and Theocracies were said not to mesh naturally with CK3's dynastic
gameplay at launch.

> ⚠️ Republic government was subsequently added to the game (Roads to Power expansion), so the
> pre-launch "doesn't fit" framing is outdated.

Inheritance overrides an existing feudal contract only when it changes liege or raises tier;
otherwise the heir's own prior contract carries over. "Gavelkind" was renamed for being
inaccurate outside the British Isles. Byzantium deliberately shipped without a bespoke
government/succession type at launch — the devs wanted real mechanics rather than a reskinned
Elective government, and stated intent to revisit it properly later (a dedicated Byzantine system
did arrive in a later update; exact patch not confirmed here). There's no Viceroyalty system —
considered too micromanagement-heavy and spammy in CK2, and any future version would be built
from scratch. Powerful vassals can force their way onto the council regardless of competence,
which is intentional friction: council seats carry strong bonuses, so vassals want them even when
incompetent. The Clan-government invasion CB requires reaching a fame level much harder than
CK2's invasion requirement, and Clan vassals expect an alliance (usually via marriage) with their
liege; Clan strength ebbs and flows over time — strong enough at its peak to rival Feudal realms,
vulnerable at its low points. Raid loot is stored on the raiding army itself and banked only once
it returns home, rather than accruing to a separate fleet treasury. See
[Realm & Succession](../02-realm-and-succession/).

## Men-at-Arms, Mercenaries, and Casus Belli

Troop numbers are visible in-game (only hidden in one specific dev-diary screenshot). Max
Men-at-Arms slots and Knight counts are calculated separately from tier and other modifiers, both
scaling up with realm size. Troops can be split across multiple armies instead of being raised all
at once. Vassals contribute levies only, never their own Men-at-Arms. Upgrading a MAA regiment's
size still only takes one slot, so with enough gold you can field a heavily professionalized army
within your slot limit. MAA effectiveness scales with regiment size rather than a separate combat-
XP system. Terrain bonuses for Men-at-Arms apply to attacker and defender alike, though the
overall Advantage math still tends to favor the defender.

## Factions & Civil Wars

Landed vassals sharing faith with a Populist Faction can join it and end up part of the resulting
split-off realm if it wins; landed characters can never join a Peasant Rabble faction. County
military power (hence faction strength) is driven by levies, indirectly tied to development.
Populist Factions always target the realm's top liege regardless of who personally holds the
land; Peasant Rabble targets the actual county holder. A vassal's own faction membership and
their counties' Populist membership track independently of each other. Non-faction vassals won't
fight for you in a civil war directly but still owe normal levies and taxes. Claimant and Liberty
factions are driven mainly by vassal opinion (roughly +30 keeps vassals out) or, alternatively, by
a high Dread value; Independence and Populist factions instead track structural issues — whether
you're the rightful liege of your direct vassals, and whether your vassals/county holders share
your culture and faith. A faction's Discontent only grows once its military power rivals yours,
and starts shrinking once pushed back under ~80%. Crushing a revolt gives affected counties a
large, ~10-year opinion boost toward their holder, discouraging repeat rebellion. A winning
claimant and the faction that installed them gain mutual opinion bonuses, and faction members get
a hook on their new liege. You can't join a faction once its rebellion has already started, but
hooks can pressure a fellow vassal into joining yours.

## Religion & Faith

Events can require either a specific Faith or just the tenets/doctrines it happens to hold — the
latter is far more common given the scope of the religion system. Clerical investiture rules are
fixed per faith; dynamic investiture and anti-papacies were a stated future-patch goal (unclear
whether since implemented — check current religion mechanics). The religious hierarchy is only
Religion → Faith, with no sub-Faith tier: Catholicism, Orthodoxy, Cathars, and Paulicians are all
co-equal Christian Faiths, and how hostile they view each other is governed separately by the
religious-hostility system, distinct from Fervor. Tenet count is UI-capped at 3 even though more
is technically moddable. Converting faith costs Piety scaled by distance — same-Faith cheapest,
cross-Religion-Family hardest — discounted by a spouse/concubine of the target faith or the
Apostate perk, and heavily penalized when converting to an unreformed pagan Faith (worse for
non-tribal rulers) or reviving an extinct religion. Celtic paganism isn't in the game; Egyptian
paganism is loosely represented via Kushitism; Gnostic Christianity has several distinct
varieties; Zoroastrianism sits in the Oriental family with unique mechanics; Magyar and Tengri
paganism are separate Faiths; Hinduism is represented as multiple distinct Faiths rather than one.
Polyandry is possible with Polygamous Marriage plus Female Dominated tenets (female rulers can
take up to 4 husbands). Pantheon Faiths pray to context-specific gods (war, harvest, fate), though
not every Faith has the full CK2-style "pick a patron god" mechanic. Slavic paganism is a single
Faith; roughly 20 Muslim Faiths exist. See [Religion & Culture](../03-religion-and-culture/).

## Custom Faith & Pagan Reformation

New custom or reformed Faiths inherit holy sites from their parent Faith. Only players can create
ahistorical custom Faiths or heresies — the AI only spawns historical heresies (Lollardy,
Waldensianism). A temporal Head of Faith can direct Great Holy Wars and keep the conquered land
personally; a spiritual (non-playable) head instead launches undirected ones and can grant gold or
claims to pious followers. A reformed pagan Faith can't be re-reformed by someone else, but
converting into it and schisming off your own branch is possible. You choose the name and icon of
a custom or reformed Faith yourself. Tenets can't be changed dynamically via a religious council
at launch — stated as a planned future addition (status unconfirmed here). Two pagan Faiths start
with Human Sacrifice. Female-dominated/enatic Faiths' AI prioritizes matrilineal marriage. The AI
reforms pagan Faiths automatically (dropping Unreformed, creating a Head of Faith) but never
customizes tenets itself. Reformed Paganism can spawn an "Old Paganism" heresy. No two Faiths can
share an identical tenet/doctrine set. The Prophet lifestyle perk halves the Piety cost of
creating or reforming a Faith. The Roman Empire exists as a creatable/reformable title. Any dead
Faith, not just Hellenism or Zunism, can be revived.

## A Medieval Tapestry

Sexuality doesn't override cultural/religious marriage norms: a gay man in a default Catholic
realm is still expected to marry a woman, since attraction mainly affects seduction, romance, and
lover status rather than the marriage obligation itself (being a spouse's lover also boosts
fertility, something a mismatched couple is less likely to get). Gender doesn't hard-gate
interactions like knighthood by itself — that's set in script and moddable — though the View on
Gender doctrine's granularity was limited at launch. The default start includes non-heterosexual
characters. A character's sexuality can only shift once, via a rare childhood "discovery" event,
and is locked afterward by design — it's deliberately not portrayed as a repeatable choice. The
Male/Female Dominated tenet governs who gets *implicit* claims (a claim a child holds while their
parent is still alive); ordinary claim inheritance is unaffected. Default sexuality distribution
is roughly 89% heterosexual, 5% homosexual, 5% bisexual, 1% asexual, and is adjustable via game
rules. Personality traits like Lustful aren't tied to sexuality — an asexual character can still
be Lustful.

## Holy Orders

The interaction preview shows whether a courtier is likely to accept joining a Holy Order or
clergy before you commit to the request. Any Faith can found Holy Orders, though cost limits most
rulers to none or very few. Order names are drawn from a per-faith/religion historical pool (e.g.
Knights Hospitaller for Christianity), falling back to a generated name once that pool runs out —
custom Faiths work the same way. A Patron of an existing Holy Order can't found a new one, which
caps proliferation. Holy Orders can hold land across multiple realms, and granting one a holding
nets the grantor a bonus.

## Fervor, Religious Hostility & Doctrine

Religious hostility between Faiths changes only via specific Tenets or Doctrines (e.g. the
Ecumenism doctrine, the Christian Syncretism tenet); at launch, only Gnostic Faiths could view
others as fully "Righteous" (may have been expanded since). Fervor is global per Faith and
recovers dynamically after heresy outbreaks, avoiding the CK2 "heresy death-spiral." Only one
custom Faith is allowed per character lifetime, with no per-campaign cap. Doctrines and tenets are
broadly moddable. Magyar and Tengri paganism have separate holy sites. The Nestorian Faith starts
present in Socotra and parts of Mongolia. Multiple pagan Faiths under a broader Religion can
reform independently of each other. Each Faith — not each broader religion — has its own Head of
Faith, so different Muslim Faiths each get their own Caliph-equivalent. Holy Orders can act as
bankers (defaulting on their loans is unwise); a patron can revoke a Holy Order's lease to erase
debt owed to them, while refusing to pay a non-patron order angers the Pope. Heretics of your own
religion tend to be disliked more than distant infidels under the hostility system. A decision
exists at launch to mend the Catholic/Orthodox schism, with other schisms flagged as possibly
mendable in future patches.

## Map Features, Map Modes, and Map Scope

Ctrl-click (and Ctrl-right-click) to preview sub-realm breakdowns still works in Realm map mode,
and every map mode has hotkeys. Development raises taxes, levies, and supply limit; armies over
their supply limit lose supply and then take attrition. Some special buildings (e.g. the Alhambra)
have levels, though the "Level 1" label persists by default even on ones that don't, like
Notre-Dame. Special/"Great Work"-style buildings are fixed to specific counties (Notre-Dame only
in Paris) — some exist at game start, others must be constructed, and they're spread across the
map as contested hotspots. Each barony holds exactly one holding out of a fixed total; not all are
built from the start, leaving room to expand. A handful of special buildings (Pyramids, Hagia
Sophia) get map-visible models. Building appearance varies visually by culture/region (e.g. India
vs. Europe).

## Cultures & Cultural Innovations

> ⚠️ Culture mechanics — innovations, cultural heads, hybrid/divergent culture creation — were
> substantially reworked in a later free update that added Cultural Traditions and Pillars. The
> specific innovation-unlock mechanics described below reflect the pre-launch system and may not
> match the current one.

There are three distinct Brythonic cultures (Cornish, Welsh, Breton) rather than one "Briton,"
and Iceland alone retains Norse culture in 1066. Character (not province) culture determines
available succession/tech options, and imposing a foreign culture is generally resented by
vassals and peasants alike. Cultural heads don't need to be independent rulers, and a culture can
even function without one, defaulting to a random fascination and modest innovation pace. New
historical cultures (e.g. Portuguese) emerge via a case-by-case mix of decisions and events,
typically inheriting shared, non-special innovations from their parent culture(s) (Norman
inherits shared French and Norse ones). Culture-specific mechanics (Basque/Zhangzhung equality,
Tanistry) travel with the people who carry them rather than being tied to geography. A culture
that gains a strong local foothold elsewhere (e.g. Irish becoming dominant across Scandinavia) can
unlock that region's cultural innovations, like Viking longships. Spousal culture doesn't affect
culture opinion by design. Dutch sits in the Central Germanic culture group despite Scandinavian
links; French remained just French/Occitan at launch. Cultural Men-at-Arms like Cataphracts are
effectively "imported" via purchase rather than trained locally by a non-matching culture. Custom
Kingdom/Empire titles are formable. A character's culture can change via education, decision, or
event. Once a culture unlocks a region-specific innovation, it keeps it permanently even if it
later relocates. Most cultures share their special innovation with a handful of related cultures
(Horse Archers); some are fully unique (Scottish Schiltron).

## Art, Portraits, and Heraldry

Character portraits reflect weight changes and pregnancy. No cavalry-specific unit models or
holding "building sprawl" shipped at launch, though both were floated as possible future
additions. Coat-of-arms "cantons" that appear to obscure charges are deliberately modeled on real
historical heraldry (e.g. the Sharingbourne arms from the c. 1348 Powell Roll). Dynastic
quartering is dynamic for cadet branches, but realm/title arms only got a handful of hand-made
historical combinations at launch rather than full dynamic quartering. There's no in-game CoA
editor at launch (unlike CK2's Ruler Designer DLC), though the underlying CoA scripting — raw
shape/color elements positioned via script — is powerful and fully moddable. The barbershop
unlocks hairstyles, hair types, hair colors, and clothing independent of a character's ethnicity.
Useful modding reference sizes: dynastic emblems are 128×128px, CoA texture elements up to
256×256 (.dds), and world map textures 8192×4096. GUI scaling is adjustable in options.

## Decisions

The butterfly-shaped icon under a portrait indicates the character's chosen Lifestyle (e.g.
praying hands for Theology). Pilgrimages must be undertaken alone, without spouse or children,
though pilgrims may encounter fellow co-religionists en route. There was no dedicated religious
festival system (Ramadan, Easter, etc.) planned for launch. See
[Decisions & Activities](../08-decisions-and-activities/).

## Modding & Scripting Notes

The `script_docs` console command dumps every trigger, effect, scope type, event target link,
modifier, and on_action to log files for reference. Localization and GUI mods still affect the
multiplayer checksum. Saved scopes (`save_scope_as` / `scope:name`) replaced CK2's event targets;
pre-triggers were dropped as largely unnecessary once mean-time-to-happen stopped requiring
constant background trigger checks. A parameterless `yearly_global_pulse` fires every January 1st
as a clean hook for maintenance effects, replacing the old CK2 trick of using the Pope as a dummy
scope. Character creation now supports reusable `scripted_character_templates`
(`common/scripted_character_templates`) instead of a fixed set of `create_character` variants per
role. New UI elements can be added under any existing interface. Title tiers above Emperor aren't
moddable (hardcoded), but new holding types, new trait tiers, and new succession-law variants
(built from existing hardcoded succession types) are. Map modding follows a CK2-style split of
map/province/history folders rather than Imperator's monolithic CSVs. Historical character IDs can
now be arbitrary strings.

## Stress

Pets can relieve stress. The AI weighs its own personality when picking options, which limits (but
doesn't eliminate) stress-inducing choices; a character can even accidentally kill themselves
while trying to cope. All characters start at Stress Level 0 (no penalty). Suicide becomes an
option for some characters at high Stress Levels, with real consequences for their successor.
Coping mechanisms range from destructive habits (frequent brothel visits risking STDs, "Lashing
Out" damaging vassal opinion) to safer ones like journaling or exercise — though even those carry
mild downside risk (e.g. a discovered journal). Extreme, sustained stress can contribute to death
via worsening health or a heart attack.

## Audio

CK3 uses a dynamic, context-reactive music and ambiance system — the soundtrack shifts with
events like entering a war — rather than one static loop, aimed at holding up over hundreds of
hours of play. Ambiance sound blends terrain-based and location-based triggers.

## Feudal Contracts

An heir inherits a dying vassal's contract only if the heir was landed at a lower tier than the
deceased; otherwise the heir's own prior contract carries over. Coinage Rights grant a vassal
+0.3 monthly development growth in their capital county at a cost of -0.02 to the liege.
Fortification Rights (where the culture innovation is unlocked) cheapen a vassal's castle-holding
build costs and grant a free fort level, at the liege's expense. A vassal with Council Rights can
freely demand a council seat (otherwise only via hooks), capped by how many seats you actually
have available to vassals. Contracts are negotiated individually per vassal — by design, to
encourage a properly tiered liege hierarchy rather than bulk edits. Taking over or vassalizing a
ruler keeps their prior contract if it was better than default; a brand-new courtier grant always
starts on default terms. Changing a contract notifies the affected party, and the AI avoids
stacking too many changes at once, though a badly-treated vassal can still rebel. Only Feudal
realms use this granular, obligation-based contract — Clan realms use a flatter contract that
scales with opinion instead, and only Feudal contracts are unaffected by opinion directly (a
resentful Feudal vassal is more likely to join a Liberty faction instead). Fine-print/contract-
option availability is set by the liege's culture innovations, not the vassal's. Vassals can push
for a Crown Authority change via faction or rebellion, but can't force an individual contract edit
that way — only through hooks or a negotiated trade (e.g. lower taxes for more troops, with some
Tyranny risk if unfair). The opinion penalty from harsh obligations is permanent as long as the
terms stand. Vassals can propose contract changes too, but must offer a fair trade in return
(unlike the liege, who can impose unfair terms at the cost of Tyranny).

## Portraits System

Body-affecting traits (Giant, Dwarf, Hunchbacked, Clubfoot, Spindly) exist alongside inheritable
height/build variation, though you can't breed toward an arbitrary trait like long arms directly.
Attractive/Ugly traits are tiered, and prettier characters age more slowly on-screen. An Inbred
trait exists without a full genetic inbreeding simulation. Dead characters appear grayed out but
remain viewable in their pre-death appearance. Disfigured or leprous characters wear masks by
default when the "hide graphical diseases" option is on. Aging speed, greying, and balding have
some randomness and inheritance. DNA is moddable, including new attachment types in principle.
New characters draw from preset ethnicities, keeping regional appearance drift in check across
generations. Beards appear abruptly at age 18 (stubble fades in gradually). Milder disease
presentation uses a generic pale/hollow look or a mask for severe cases. Body type (skinny/chubby/
muscular) has some inheritance but is mostly driven by in-game factors; height loosely follows
real medieval-population distributions (shorter on average, with occasional tall outliers).
Portrait animations can be disabled for performance. Hair-color inheritance is a simplified
coin-flip between parents rather than true genetics. Normal-height characters without
Giant/Dwarf traits still vary meaningfully in height, which is itself inherited.

## Performance & AI

Script execution is heavily parallelized, which is the main performance lever; some triggers and
list-builders trade flexibility for better performance. There's no separate AI difficulty
setting — only an overall game difficulty, which mainly boosts the AI's resources rather than
making its decision-making "smarter," since making AI reliably play better at higher settings is
a hard problem in complex strategy games. The AI simulates fog of war to some extent (it stops
precisely tracking you once you're hidden, though it stays vaguely aware of army sizes).
Characters are no longer silently deleted for lacking relevance as in CK2 — unwanted characters
drift into the wanderer pool instead, and their health slowly declines the longer they stay
unplaced. AI personality is derived from each character's own traits rather than a global preset,
so there's no single toggle to make "all AI" uniformly aggressive or passive.

## Legacies

Renown accrual rewards spreading a dynasty widely — marrying into powerful foreign houses,
branching lines — over pure map-painting; a "normal" game was estimated at roughly 1–2.5
completed Legacy lines, more with deliberate spreading. Dynasties don't start with legacies
pre-unlocked based on their real history (e.g. the Seljuks don't start with Warfare legacies),
though prominent families still accrue Renown faster once playing. An AI Dynasty Head who
inherits the role sticks to the previous head's chosen Legacy path rather than switching. The Kin
Legacy's fertility bonus was tuned down substantially during development (from 25% to 10%) after
early testing overpopulated the game world. Any landed dynasty member generates a small trickle of
Renown, but unlocking Legacies requires actively spreading the dynasty rather than picking a
"focus." Domain control modifiers apply only to your own personal domain, not additively across
every title held by dynasty members. See [Rulers & Dynasties](../07-rulers-and-dynasties/).

## Achievements

Ironman mode is required for achievements. The "Sibling Rivalry" achievement can be completed
with any of the eligible Jimena siblings — Urraca, Sancho, Alfonso, or Garcia (Elvira qualifies in
principle but starts unlanded and unplayable). CK3 doesn't have an EU4-style "endgame tags"
system, but historical formables like India, Outremer, and Slavia exist as decision-based title
formations. See [Achievements](../09-achievements/) for the full current list and requirements.
