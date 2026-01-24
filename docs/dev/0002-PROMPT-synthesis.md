# Synthesis Prompt: Reconciling Multiple Sources

## Purpose

This prompt merges concept cards extracted from multiple sources into unified, authoritative cards. It handles differing definitions, notation, emphasis, and coverage — producing a single canonical treatment of each concept.

**This prompt sits between extraction and guide generation:**

```
Source A ──→ [EXTRACTION] ──→ Cards A ──┐
Source B ──→ [EXTRACTION] ──→ Cards B ──┼──→ [SYNTHESIS] ──→ Unified Cards ──→ [GUIDE GEN]
Source C ──→ [EXTRACTION] ──→ Cards C ──┘
```

---

## When to Use This Prompt

Use this prompt when you have:
- Concept cards for the **same topic** (e.g., Category Theory) from **multiple sources**
- Cards that may cover **overlapping but not identical** sets of concepts
- **Differing notation, emphasis, or even definitions** across sources

**Do NOT use this prompt for:**
- Cards from different fields (don't merge a group theory card with a category theory card)
- A single source (no synthesis needed)

---

## The Prompt

```
You are synthesizing concept cards from multiple mathematical sources into unified, authoritative reference cards. Your goal is to produce ONE canonical card per concept that combines the best of all sources.

## Source Information

<source_a>
**Source:** [TITLE A]
**Author(s):** [AUTHORS A]
**Perspective:** [e.g., "algebraic/abstract", "computational", "geometric", etc.]

[PASTE CONCEPT CARDS FROM SOURCE A]
</source_a>

<source_b>
**Source:** [TITLE B]
**Author(s):** [AUTHORS B]  
**Perspective:** [e.g., "pedagogical", "applications-focused", etc.]

[PASTE CONCEPT CARDS FROM SOURCE B]
</source_b>

<source_c>
**Source:** [TITLE C]
**Author(s):** [AUTHORS C]
**Perspective:** [e.g., "encyclopedic/reference", "research-level", etc.]

[PASTE CONCEPT CARDS FROM SOURCE C]
</source_c>

[Add more sources as needed]

## Synthesis Instructions

### Step 1: Inventory

First, produce a concept inventory table:

| Concept | Source A | Source B | Source C | Notes |
|---------|----------|----------|----------|-------|
| [concept] | ✓ | ✓ | ✗ | |
| [concept] | ✓ | ✓ | ✓ | Definitions differ |
| [concept] | ✗ | ✓ | ✓ | |
| ... | | | | |

Mark:
- ✓ = source covers this concept
- ✗ = source does not cover this concept
- Add notes for: differing definitions, notation conflicts, different emphasis

### Step 2: Classify Differences

For each concept covered by multiple sources, classify the relationship:

**A. Identical** — Sources agree completely (possibly different words, but same meaning)
→ Action: Use clearest presentation

**B. Complementary** — Sources cover different aspects, no conflict
→ Action: Merge by combining content

**C. Notational** — Same concept, different notation  
→ Action: Standardize to NOTATION.md, note variants

**D. Equivalent characterizations** — Different but provably equivalent definitions
→ Action: Pick primary definition, list others as "equivalent characterizations"

**E. Genuine disagreement** — Sources actually conflict (rare in math, but possible in conventions or edge cases)
→ Action: Note the disagreement explicitly, state which convention we adopt and why

**F. Different scope** — One source defines more generally/restrictively than another
→ Action: Use most appropriate scope for our purposes, note alternatives

### Step 3: Synthesize Each Concept

For each concept, produce a unified card following this enhanced structure:

---

## Concept: [Name]

### Definition

[The canonical definition for this skill. Choose based on:
1. Precision (mathematically exact)
2. Generality (appropriate level — not too narrow, not too abstract)
3. Usability (can we work with it?)
]

**Source:** [Primary source for this definition]

**Alternative definitions:**
- [Source B] defines this as: [alternative]
- [Source C] uses: [alternative]

[Note if these are equivalent or genuinely different. If equivalent, optionally sketch why.]

### Notation

**Standard (this skill):** [notation per NOTATION.md]

**Variants:**
| Notation | Used by | Notes |
|----------|---------|-------|
| [variant] | [Source A] | |
| [variant] | [Source B] | [when this might be preferred] |

### Intuition

[Synthesize the best intuitive explanations from all sources. Often different sources illuminate different aspects — combine them.]

**From [Source A]:** [their angle]
**From [Source B]:** [their angle]

[Then give a unified intuitive summary.]

### Key Examples

[Collect the best examples from all sources. Prefer:
- Canonical examples that appear in multiple sources (these are clearly important)
- Complementary examples that illustrate different aspects
- Concrete, computable examples over abstract ones
]

1. **[Example]** — [description] *(from [Source])*
2. **[Example]** — [description] *(from [Source])*
3. **[Example]** — [description] *(synthesized/original)*

### Non-Examples / Counterexamples

[Collect from all sources]

### Equivalent Characterizations

[This is where "different definitions" become a feature, not a bug. List all equivalent ways to define/characterize the concept.]

1. [Characterization 1] *(Source A's definition)*
2. [Characterization 2] *(Source B's definition)*
3. [Characterization 3] *(Source C's approach)*

**Equivalence:** [Brief note on why these are equivalent, or reference to theorem]

### Key Theorems

[Merge theorem lists. For the same theorem stated differently:]
- Use the clearest/most general statement
- Note if sources prove it differently (might inform proof techniques section)

**Theorem ([Name]).** [Statement]
- *Appears in:* [Source A §X, Source B §Y]
- *Proof approach:* [Note if sources use different proofs — both might be useful]

### Proof Techniques

[Synthesize across sources — different authors often emphasize different techniques]

**From [Source A]:** [technique/approach]
**From [Source B]:** [technique/approach]

[Unified guidance]

### Common Errors / Gotchas

[Merge all warnings from all sources — these are gold]

### Prerequisites

[Union of prerequisites from all sources, but minimize — only list direct prerequisites]

### Leads To

[Union of downstream concepts]

### Connections

[Synthesize — different sources may emphasize different connections]

### Source Concordance

[For users who want to consult original sources]

| Aspect | Source A | Source B | Source C |
|--------|----------|----------|----------|
| Definition | §X.Y, p.N | §A.B, p.M | [article name] |
| Main theorem | Thm X.Y | Prop A.B | — |
| Examples | Ex X.Y.Z | §A.B | — |

---

### Step 4: Handle Gaps

For concepts that appear in only ONE source:

- **If it's a core concept:** Keep it, note that other sources don't cover it, consider whether this is a gap in other sources or a specialty topic
- **If it's peripheral:** Consider whether to include (is it needed for our guides?)
- **If it's research-level:** Probably exclude unless directly relevant

For concepts where sources DISAGREE:

- **State both positions clearly**
- **Indicate which convention this skill adopts**
- **Explain the choice** (e.g., "We follow Source A because it aligns with HoTT conventions")

### Step 5: Quality Checks

Before finalizing:

- [ ] **Every concept has ONE definition** (alternatives listed as "equivalent characterizations")
- [ ] **Notation is standardized** to NOTATION.md
- [ ] **No contradictions** — if sources disagree, it's flagged and resolved
- [ ] **Attribution is clear** — know where each piece came from
- [ ] **Coverage is complete** — no concept from any source is lost without reason
- [ ] **Examples are deduplicated** — don't repeat the same example twice

---

## Example: Synthesizing "Adjunction"

### Input

**Source A (Riehl):** Defines via Hom-set bijection, emphasizes naturality, gives free-forgetful as main example.

**Source B (Leinster):** Defines via unit/counit, emphasizes universal property perspective, gives geometric realization example.

**Source C (nLab):** Gives five equivalent definitions, extensive list of examples, connects to 2-category theory.

### Output

---

## Concept: Adjunction

### Definition

Let F : C → D and G : D → C be functors. An **adjunction** F ⊣ G consists of a natural isomorphism

Hom_D(F(X), Y) ≅ Hom_C(X, G(Y))

for all X ∈ C and Y ∈ D.

**Source:** Riehl, Definition 4.1.1

**Alternative definitions:**
- **Unit/counit (Leinster):** Natural transformations η : 1_C → GF and ε : FG → 1_D satisfying triangle identities
- **Universal arrows (nLab):** For each X in C, a universal arrow from X to G

These are equivalent (Riehl Proposition 4.2.6).

### Notation

**Standard (this skill):** F ⊣ G (F is left adjoint to G)

**Variants:**
| Notation | Used by | Notes |
|----------|---------|-------|
| (F, G, η, ε) | Leinster, when emphasizing unit/counit | |
| (F, G, φ) | Some texts | φ is the Hom-set bijection |

### Intuition

**From Riehl:** "Adjunctions formalize the notion of 'optimal solution' — the left adjoint freely generates structure, the right adjoint forgets it."

**From Leinster:** "Think of the unit as 'inserting generators' and the counit as 'evaluating.'"

**From nLab:** "Adjunctions are ubiquitous because they capture universal properties — nearly every important construction is an adjoint."

**Unified:** An adjunction is a precise way of saying two functors are "optimally matched." F freely builds D-structure from C-data; G extracts the underlying C-data from D-structure. The adjunction says: giving a D-map from "free" to Y is exactly the same as giving a C-map from the original to "underlying of Y."

### Key Examples

1. **Free-forgetful (groups):** F : Set → Grp, U : Grp → Set, F ⊣ U *(all sources)*
2. **Product-Hom (currying):** (– × A) ⊣ Hom(A, –) *(Riehl, Leinster)*
3. **Geometric realization ⊣ Singular:** |–| ⊣ Sing *(Leinster, nLab)*
4. **Discrete ⊣ Forgetful ⊣ Indiscrete:** For Top → Set *(nLab)*
5. **Tensor-Hom:** (– ⊗ M) ⊣ Hom(M, –) for modules *(nLab)*

### Equivalent Characterizations

1. **Hom-set bijection** (primary definition above)
2. **Unit and counit** with triangle identities
3. **Universal arrows:** For each X, a universal arrow from X to G
4. **Initial object in comma category:** (F↓D)(X, –) has initial object for each X
5. **Representability:** G represents Hom_D(F(–), Y) for each Y

**Equivalence:** Riehl §4.2 proves (1)⟺(2). nLab proves all five equivalent.

### Key Theorems

**Theorem (RAPL).** Right adjoints preserve limits.
- *Appears in:* Riehl 4.5.2, Leinster 6.3.1, nLab
- *Proof approach:* Riehl uses Hom-set characterization; Leinster uses universal property

**Theorem.** Every adjunction induces a monad GF on C and a comonad FG on D.
- *Appears in:* Riehl §5.2, Leinster §5.2, nLab

### Proof Techniques

**From Riehl:** To show F ⊣ G, establish the Hom-set bijection and verify naturality.

**From Leinster:** To show F ⊣ G, construct η and ε and check triangle identities (often easier for concrete examples).

**Unified:** 
- For abstract existence: Use adjoint functor theorem (if hypotheses met)
- For concrete verification: Unit/counit approach is often cleanest
- To *use* an adjunction: Apply RAPL/LAPL, or use the Hom-set bijection to translate problems

### Common Errors / Gotchas

- **Confusing left/right:** (all sources) "Free" is left, "forgetful" is right. Mnemonic: "Right adjoints are righteous" (preserve limits).
- **Forgetting naturality:** (Riehl) The bijection must be natural in both variables.
- **Unit/counit direction:** (Leinster) η : 1 → GF, ε : FG → 1 — the "free then forget" gets the unit.

### Source Concordance

| Aspect | Riehl | Leinster | nLab |
|--------|-------|----------|------|
| Definition | Def 4.1.1 | Def 2.3.6 | [adjunction] |
| RAPL | Prop 4.5.2 | Prop 6.3.1 | [adjoint functor] |
| Monad connection | §5.2 | §5.2 | [monad] |

---

Now synthesize all concepts from the provided source cards.
```

---

## Handling Special Cases

### When Sources Genuinely Conflict

Rare in mathematics, but can happen with:
- **Conventions:** Is 0 a natural number? Does "ring" require a unit?
- **Terminology:** "Regular" means different things in different contexts
- **Scope:** Does "space" mean topological space, CW complex, or compactly generated?

**Resolution template:**

```markdown
### Scope/Convention Note

Sources differ on [issue]:
- **Source A:** [their convention]
- **Source B:** [their convention]

**This skill adopts:** [chosen convention]

**Rationale:** [why — e.g., "aligns with HoTT usage" or "more common in modern literature"]

**Caution:** When consulting external resources, verify their convention.
```

### When One Source is Clearly Superior

Sometimes one source simply treats a topic better:
- More examples
- Clearer proof
- Better motivation

**It's fine to lean heavily on that source for that concept.** Note it in the concordance so users know where to look for more depth.

### When a Concept is Specialized

If only one source covers a concept (e.g., nLab covers something research-level that textbooks skip):

```markdown
### Note

This concept appears only in [Source]. It is [included/excluded] in this skill because [reason].

[If included:] For complete treatment, consult [Source] directly.
```

---

## Output Structure

After synthesis, you should have:

```
synthesized/
├── [field]/
│   ├── _SYNTHESIS_NOTES.md    # Inventory table, decisions made, conflicts resolved
│   ├── [concept-1].md         # Unified card
│   ├── [concept-2].md         # Unified card
│   └── ...
```

The `_SYNTHESIS_NOTES.md` file documents:
- Which sources contributed to each concept
- How conflicts were resolved
- What was excluded and why

This creates an audit trail for future updates.

---

## Integration with Workflow

**Updated pipeline:**

```
Phase 2: Conversion
       │
       ▼
Phase 3: Extraction (per source)
       │
       ├── Source A → Cards A
       ├── Source B → Cards B
       └── Source C → Cards C
       │
       ▼
Phase 3.5: Synthesis (NEW) ← YOU ARE HERE
       │
       └── Unified Cards
       │
       ▼
Phase 4: Guide Generation
       │
       ▼
Phase 5: SKILL.md Assembly
```

---

## Checklist Before Moving to Guide Generation

- [ ] All concepts from all sources are accounted for (included or explicitly excluded)
- [ ] Every unified card has exactly ONE primary definition
- [ ] Notation is fully standardized
- [ ] Conflicts are resolved and documented
- [ ] Source concordance is complete for each card
- [ ] _SYNTHESIS_NOTES.md documents all decisions

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-23 | Initial prompt |
