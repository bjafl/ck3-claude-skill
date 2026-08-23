---
title: Attributes
category: character-mechanics
tags: [character, attributes, skills, health, stress]
game_version: "1.19"
dlc: []
sources: [https://ck3.paradoxwikis.com/Attributes]
---

Attributes represent core character statistics that define how capable characters are at various tasks. They determine combat prowess, management abilities, negotiation skills, and overall health status.

## Age

Characters are children until age 16, becoming adults thereafter. Natural death from old age occurs after age 60 (or from poor health beforehand with reason "Natural Causes"). Each starting character unlocks lifestyle perks based on age.

- At age 25+: 7.5% yearly chance to lose 0.125 health, increasing by 2.2% annually
- At age 45+: 10% yearly chance to lose 1 prowess, increasing by 1.5% annually (prevented by completing Kin legacy)

## Skills

Skills represent expertise across five main areas: diplomacy, martial, stewardship, intrigue, and learning. Prowess is a secondary skill for personal combat. Characters begin with 0-10 base skill points (partially hereditary), gain up to 4 additional points between ages 6-16 (hereditary), and can reach a maximum of 100.

### Skill effects per level

| Skill | Effect per level | [Khans of the Steppe] Nomadic bonus |
|---|---|---|
| Diplomacy | +1% Monthly Prestige (−8% at Level 0) +1 General Opinion (−8 at Level 0) Increases Diplomacy Scheme effectiveness Increases initial legitimacy | +1% Herd Gain (−8% at Level 0) |
| Martial | −1.00% Army Gold Maintenance (+8% at Level 0) +1 Knight (per 5 Levels) +1% Army Toughness (−8% at Level 0) +2.5% Levy Reinforcement Rate (−20% at Level 0) +1 Travel Safety +1 Advantage commanding armies | +0.5% Herd Conversion into Horde Riders (−4% at Level 0) |
| Stewardship | +2% Domain Taxes (−16% at Level 0) +4% Domicile Income (−32% at Level 0) +1 Travel Speed +1% Barter Goods | +2% Herd Income (−16% at Level 0) |
| Intrigue | +2% Scheme Secrecy −0.5% Enemy Scheme Secrecy +1 Scheme Advantage (per 5 Levels above 15) +1% Initial Success Chance +1% Imprisonment Success Chance | — |
| Learning | +0.10 Monthly Piety −1% Conversion Cost +1 Demand Conversion Acceptance +0.2 Foreign Language Limit Reduces Crown Authority cost | +2% County Fertility Growth (−16% at Level 0) |
| Prowess | +50 Damage as knight +10 Toughness as knight Determines combat moves in duels Determines likelihood of injury/death in battle Determines muscle mass in appearance | — |

### Skill rating thresholds

| Values | Description |
|---|---|
| 0–4 | Terrible |
| 5–8 | Poor |
| 9–12 | Average |
| 13–16 | Good |
| 17–68 | Excellent |
| 69 | Nice |
| 70–100 | Excellent |

## Dread

Dread measures how feared a ruler is by subjects, ranging 0-100 (or 0-150 for Nomadic and Meritocratic Khanate rulers). High dread relative to a character's boldness makes them intimidated or terrified, allowing diplomatic actions to succeed despite negative opinion.

Dread gains from fear-inspiring actions (torture, execution) and naturally drifts at 0.5 per month toward a character's "natural dread" value. The Graven Infamous lifestyle perk prevents dread decay.

Each character has hidden boldness determined primarily by traits (Brave never intimidated; Craven always terrified):
- Intimidated when target dread exceeds own boldness by 20+
- Terrified when target dread exceeds own boldness by 45+

### Intimidation and terror effects

| Interaction | Intimidated bonus | Terrified bonus |
|---|---|---|
| Arrange marriage | +75 | +150 |
| Blackmail | +50 | +100 |
| Negotiate alliance | +50 | +100 |
| Offer guardianship | +50 | +100 |
| Offer ward | +50 | +100 |
| Ransom | +40 | +100 |
| Ask to take vows | +25 | +50 |
| Imprison | +25 | +50 |
| Retract vassal | +25 | +50 |
| Revoke title | +25 | +50 |
| Demand conversion | +10 | +20 |
| Offer vassalage | +10 | +20 |
| Marry | −50 | −75 |

### Natural dread modifiers

Base is 0. Key sources: Sadistic trait (+35), Greatest of Khans (+50), Wrathful (+20), Cannibal (+20), Compassionate (−15), multiple illness traits (−5 to −30).

## Health

Male characters begin with 4.5–4.9 health; females with 5.0–5.4. Starting at age 25, annual -0.125 health chance increases 2.2% yearly.

| Health level | Can die | Range |
|---|---|---|
| Dying | Yes | < 0 |
| Near Death | Yes | 0 ≤ health < 1 |
| Poor | Yes | 1 ≤ health < 3 |
| Fine | No | 3 ≤ health < 5 |
| Good | No | 5 ≤ health < 7 |
| Excellent | No | ≥ 7 |

### Health penalties and boosts

Penalties range from "The Reaper Approaches" (≤−6) to "Tiny Health Penalty" (−0.25 to 0). Boosts range from "Small Health Boost" (+0 to 0.25) to "Godlike Health Boost" (≥+2). Disease resistance negates health penalties equal to its value.

### Death causes

- Low health state chance tick
- Murder scheme success
- Suicide decision chance
- Battle or duel injury (prowess-dependent)
- Siege capture
- Execution as prisoner
- Events

## Fertility

Fertility represents pregnancy likelihood. Married/lover couples with opposite sexes have monthly pregnancy chance based on average fertility (base 50%), modified by traits and age. Pregnancy chance monthly = (average fertility × 4.75)%.

| Age \ Gender | 16–25 | 26–30 | 31–35 | 36–40 | 41–45 | 46–50 | 51–60 | 61–70 | 70+ |
|---|---|---|---|---|---|---|---|---|---|
| Male | 1.0 | 1.0 | 1.0 | 0.9 | 0.8 | 0.8 | 0.7 | 0.6 | 0.5 |
| Female | 1.0 | 0.9 | 0.7 | 0.5 | 0.33 | No | No | No | No |

- Concubines/secondary spouses have 50% fertility
- Mothers lose 5% per childbirth
- Non-ruler characters lose 15% fertility
- Male cap: 9 living children plus 2 per additional consort/wife (max 15 with 4 wives)
- Female cap: 9 children

### Pregnancy complications

Women show pregnancy at month 2 (−2 penalty) and give birth month 10. Dynasty Legacy "Kin" Level-3 reduces complications by 25%; Faith tenet "Sacred Childbirth" reduces by 50%.

## Stress

Stress ranges 0-400 and reflects mental strain from personality-conflicting decisions, grief, imprisonment, and torture. High stress imposes penalties and triggers mental breaks at 100, 200, 300, and 400 thresholds.

| Stress level | Fertility | Health penalty | Suicide option | Mental breaks |
|---|---|---|---|---|
| 0–99 | 0 | None | No | None |
| 100–199 | −10% | None | No | Coping mechanism |
| 200–299 | −30% | Major (−1) | No | Coping mechanism, other traits |
| 300–399 | −50% | Severe (−2) | Yes | Wrathful, Lunatic, Murderer, Death, Abdication |

Mental breaks trigger once per 5-year minimum (8 with Mental Resilience perk). Characters gain coping mechanism traits granting +20% stress loss and stress-reducing decisions. Certain perks reward high stress (Thriving in Chaos: +4 Martial/Intrigue, +6 Prowess per stress level).

## Languages

Known languages reduce cultural opinion penalties by 50%. Each character knows their own culture's language. Foreign language limit starts at 1 and increases by 1 per 5 Learning. Exceeding the limit causes yearly risk of forgetting a language or gaining stress (+2 if Lazy).

## Legitimacy

Legitimacy measures a ruler's right to govern, ranging 0-2800 across 8 levels (plus special Mandala/Nomadic variants). Gained through title creation, releasing high-ranked prisoners, court holding, attending activities, war victories. Lost through title loss, tyrannical actions, faction demands, discovered schemes, excommunication, marrying Lowborn (primary spouse), and civil war losses.

Starting legitimacy scales with Dynasty Splendor Level and Court Grandeur. High Diplomacy, Just/Diplomat/Born in the Purple traits increase it. Inbred and sin traits reduce it.

Rulers with Administrative, Celestial, Meritocratic, Meritocratic Khanate, or Ritsuryō governments only have Legitimacy if independent.

## Domain

Domain Limit determines holdings providing efficient taxes and levies. Additional holdings lose production after 1 year. Base limit varies by government type and increases with:

**Standard governments (Feudal, Clan, Tribal, etc.):**
- Title rank: +2 Count, +2 Duke, +3 King, +4 Emperor, +5 Hegemon
- Education level: +1 to +3 based on level
- Lifestyle perks: +1 each
- Dynasty Legacy completion and special artifacts: +1 to +2

**Nomadic/Mandala/Wanua/Ritsuryō:** Stricter limits increased by dominance law, temple buildings, fort buildings, or manor buildings.

## Governor efficiency

Appears only in Administrative, Celestial, Ritsuryō, Meritocratic governments (−50% to +50%). Affects domain taxes, levies, and men-at-arms effectiveness. Base −100, increased by skill (+1.7 per point), education traits (+2 to +4), Governor trait (+3 to +12), and estate upgrades (+10%).

## Merit

Replaces Legitimacy for certain vassal government types. Vassals have Career Paths and Merit Ranks. On vassal death, titles pass to highest Merit Rank with same path (liege can revoke). Merit Rank limited by passed exams (Provincial +2, Metropolitan +2, Palace +3).

| Merit rank | Min merit | Max title | Movement power |
|---|---|---|---|
| No Rank | 0 | Barony | — |
| Rank 9 | 100 | County | +10 |
| Rank 8 | 250 | County | +20 |
| Rank 7 | 750 | Duchy | +30 |
| Rank 6 | 1500 | Duchy | +40 |
| Rank 5 | 2500 | Kingdom | +50 |
| Rank 4 | 4000 | Kingdom | +60 |
| Rank 3 | 5500 | Empire | +70 |
| Rank 2 | 7500 | Empire | +80 |
| Rank 1 | 9500 | Empire | +90 |

## Weight

Hidden weight ranges −100% to +100%. Below −50% grants Malnourished modifier and Gain Weight decision. Above +50% grants Obese health penalty and Lose Weight decision. Drifts by 5% twice yearly toward default based on traits and age (Diligent/Athletic slow gain; Lazy/Gluttonous increase it).

## Education

Ages 0-6: Parents select Education Focus (defaulting to Childhood trait attributes). Ages 6-16: Hidden education score increases (+2 per birthday, 10 chances, plus bonuses). At 16: Acquire education trait based on score.

**Guardian bonuses to education:**
- Guardian's relevant skill × 0.4
- Guardian's learning × 0.2
- Intelligence traits (Quick/Shrewd +10, Genius +20; Slow/Stupid −10, Imbecile −20)
- Matching Childhood trait +20; mismatching −20
- University in realm: 60% +2 points, 40% +3 points
- Court Tutor: +2 to +4 points
- Dynasty Legacy "Kin" Level-2: Guaranteed +2, 60% chance +3

**Martial education:** With Knighthood innovation and appropriate gender, also grants Prowess education trait (unaffected by guardian modifiers, only child traits).

## Obedience

Only Meritocratic Khanate and Nomadic governments. Obedient vassals don't join factions against liege, don't start hostile schemes, and migrate with liege. Obedience can be ensured 15 years by paying Herd, Gold, Dread, or a hook.

Always Obedient: Primary heir, underage, blood sibling, best friend, Herder, Paiza artifact
Always Disobedient: Nemesis, superior military strength, superior Herd, lost humiliation, recent war

| Rank | Threshold |
|---|---|
| Count | 50 |
| Duke | 70 |
| King | 100 |
| Emperor | 150 |
