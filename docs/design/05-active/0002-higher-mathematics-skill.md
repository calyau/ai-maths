---
number: 2
title: "Higher Mathematics SKILL.md Development Workflow"
author: "some authors"
component: All
tags: [change-me]
created: 2026-01-24
updated: 2026-01-24
state: Active
supersedes: null
superseded-by: null
version: 1.0
---

# Higher Mathematics SKILL.md Development Workflow

## Project Goal

Create a sophisticated, AI-optimized knowledge base covering **Group Theory**, **Type Theory**, **Category Theory**, and **Homotopy Theory** — enabling Claude to correctly assist with exploration of these interconnected mathematical fields over an extended period.

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: SOURCE ACQUISITION                                                │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                               │
│  │  HTML    │    │  LaTeX   │    │   PDF    │                               │
│  │ (prefer) │    │ (good)   │    │ (last)   │                               │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘                               │
│       └───────────────┼───────────────┘                                     │
│                       ▼                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  PHASE 2: CONVERSION & NORMALIZATION                                        │
│                 ┌─────────────┐                                             │
│                 │  Markdown   │                                             │
│                 │  + Unicode  │                                             │
│                 │  or ASCII   │                                             │
│                 └──────┬──────┘                                             │
│                        │                                                    │
│              ┌─────────┴─────────┐                                          │
│              ▼                   ▼                                          │
│       ┌────────────┐     ┌─────────────┐                                    │
│       │ NOTATION.md│     │ sources/*.md│                                    │
│       │ (standard) │     │ (converted) │                                    │
│       └────────────┘     └──────┬──────┘                                    │
│                                 │                                           │
├─────────────────────────────────┼───────────────────────────────────────────┤
│  PHASE 3: EXTRACTION            │                                           │
│                                 ▼                                           │
│                    ┌────────────────────┐                                   │
│                    │ EXTRACTION PROMPT  │                                   │
│                    │ (process sources)  │                                   │
│                    └─────────┬──────────┘                                   │
│                              │                                              │
│                              ▼                                              │
│                    ┌────────────────────┐                                   │
│                    │  Concept Cards     │                                   │
│                    │  (per source)      │                                   │
│                    └─────────┬──────────┘                                   │
│                              │                                              │
├──────────────────────────────┼──────────────────────────────────────────────┤
│  PHASE 3.5: SYNTHESIS        │                                              │
│                              ▼                                              │
│                    ┌────────────────────┐                                   │
│                    │ SYNTHESIS PROMPT   │                                   │
│                    │ (merge sources,    │                                   │
│                    │  reconcile diffs)  │                                   │
│                    └─────────┬──────────┘                                   │
│                              │                                              │
│                              ▼                                              │
│                    ┌────────────────────┐                                   │
│                    │  Unified Cards     │                                   │
│                    │  (one per concept) │                                   │
│                    └─────────┬──────────┘                                   │
│                              │                                              │
├──────────────────────────────┼──────────────────────────────────────────────┤
│  PHASE 4: GUIDE GENERATION   │                                              │
│                              ▼                                              │
│                    ┌────────────────────┐                                   │
│                    │ GUIDE GEN PROMPT   │                                   │
│                    │ (build guides from │                                   │
│                    │  unified cards)    │                                   │
│                    └─────────┬──────────┘                                   │
│                              │                                              │
│                              ▼                                              │
│                    ┌────────────────────┐                                   │
│                    │  Topic Guides      │                                   │
│                    │  (2-4k tokens ea)  │                                   │
│                    └─────────┬──────────┘                                   │
│                              │                                              │
├──────────────────────────────┼──────────────────────────────────────────────┤
│  PHASE 5: SKILL ASSEMBLY     │                                              │
│                              ▼                                              │
│                    ┌────────────────────┐                                   │
│                    │    SKILL.md        │                                   │
│                    │  (entry point)     │                                   │
│                    └────────────────────┘                                   │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  PHASE 6: VALIDATION                                                        │
│                    ┌────────────────────┐                                   │
│                    │   Test Problems    │                                   │
│                    │   (10-20 per area) │                                   │
│                    └────────────────────┘                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Source Acquisition

### Priority Order for Source Formats

| Priority | Format | Reason |
|----------|--------|--------|
| 1 | HTML | Cleanest conversion, structure preserved |
| 2 | LaTeX source | Math notation intact, can render to multiple formats |
| 3 | PDF | Last resort — math notation often mangles |

### Primary Sources by Field

#### Group Theory
| Source | Author(s) | Format | URL |
|--------|-----------|--------|-----|
| Group Theory (lecture notes) | J.S. Milne | PDF | https://www.jmilne.org/math/CourseNotes/GT.pdf |
| Abstract Algebra: Theory and Applications | Tom Judson | HTML + PDF | http://abstract.ups.edu/ |

#### Type Theory
| Source | Author(s) | Format | URL |
|--------|-----------|--------|-----|
| Intuitionistic Type Theory (1984) | Per Martin-Löf | PDF | https://archive-pml.github.io/martin-lof/pdfs/Bibliopolis-Book-retypeset-1984.pdf |
| Programming in Martin-Löf's Type Theory | Nordström, Petersson, Smith | PDF | https://www.cse.chalmers.se/research/group/logic/book/book.pdf |
| PLFA | Wadler, Kokke, Siek | Literate Agda/HTML | https://plfa.github.io/ |

#### Category Theory
| Source | Author(s) | Format | URL |
|--------|-----------|--------|-----|
| Category Theory in Context | Emily Riehl | PDF | https://emilyriehl.github.io/files/context.pdf |
| Basic Category Theory | Tom Leinster | PDF (LaTeX on arXiv) | https://arxiv.org/abs/1612.09375 |
| nLab | Community | HTML (wiki) | https://ncatlab.org/ |

#### Homotopy Theory / HoTT
| Source | Author(s) | Format | URL |
|--------|-----------|--------|-----|
| Algebraic Topology | Allen Hatcher | PDF | https://pi.math.cornell.edu/~hatcher/AT/AT.pdf |
| HoTT Book | Univalent Foundations Program | PDF + LaTeX (GitHub) | https://homotopytypetheory.org/book/ |
| Introduction to Homotopy Type Theory | Egbert Rijke | PDF | https://ncatlab.org/nlab/files/Rijke-IntroductionHoTT-2018.pdf |

### Source Versioning

Document the exact version/date of each source:

```markdown
## Source Versions

| Source | Version/Edition | Date Retrieved | Notes |
|--------|-----------------|----------------|-------|
| Hatcher Algebraic Topology | 2002, corrections through 2024 | YYYY-MM-DD | |
| HoTT Book | first-edition-1277-g3274cb3 | YYYY-MM-DD | |
| ... | | | |
```

---

## Phase 2: Conversion & Normalization

### Conversion Tools (Suggested)

- **PDF → Markdown**: `marker`, `mathpix`, or manual with `pdftotext` + cleanup
- **HTML → Markdown**: `pandoc`, custom scrapers for nLab
- **LaTeX → Markdown**: `pandoc` with `--mathjax` or custom processing

### Notation Normalization

Create `NOTATION.md` with consistent conventions. All converted sources must conform.

#### Option A: Unicode Math (Preferred for Readability)
```
∀  — universal quantifier
∃  — existential quantifier
→  — function arrow / implication
←  — reverse arrow
↔  — bi-implication / isomorphism
∘  — composition
×  — product
⊕  — coproduct / direct sum
≃  — equivalence
≅  — isomorphism
≡  — definitional equality / identity
Σ  — dependent sum
Π  — dependent product
λ  — lambda
∈  — element of
⊆  — subset
∅  — empty set
ℕ  — natural numbers
ℤ  — integers
ℝ  — reals
```

#### Option B: ASCII Fallback (Maximum Compatibility)
```
forall   — universal quantifier
exists   — existential quantifier
->       — function arrow / implication
<-       — reverse arrow
<->      — bi-implication
.        — composition (or `∘` if supported)
*        — product (context-dependent)
+        — coproduct
~=       — equivalence
~==      — isomorphism
==       — definitional equality
Sigma    — dependent sum
Pi       — dependent product
\x.      — lambda
in       — element of
subseteq — subset
{}       — empty set
Nat      — natural numbers
Int      — integers
Real     — reals
```

#### Field-Specific Notation

**Category Theory:**
```
C, D, E         — categories
Hom(X,Y)        — morphisms from X to Y
F : C → D       — functor
η : F ⇒ G       — natural transformation
⊣              — adjunction (F ⊣ G means F left adjoint to G)
lim, colim      — limits and colimits
```

**Type Theory:**
```
Γ ⊢ a : A       — in context Γ, term a has type A
A × B           — product type
A + B           — sum type
Π(x:A).B        — dependent product
Σ(x:A).B        — dependent sum
Id_A(x,y)       — identity type
refl            — reflexivity term
```

**Homotopy Theory:**
```
π_n(X)          — n-th homotopy group
[X,Y]           — homotopy classes of maps
≃              — homotopy equivalence
~              — homotopic
*               — basepoint
∧              — smash product
∨              — wedge sum
```

### Quality Checklist for Converted Sources

- [ ] All math notation renders correctly or uses consistent ASCII fallback
- [ ] Section structure preserved (headers, subsections)
- [ ] Theorem/Definition/Lemma/Proof blocks clearly marked
- [ ] Cross-references converted to internal links where possible
- [ ] Diagrams described or preserved as images with alt-text
- [ ] No OCR artifacts or garbled text
- [ ] Consistent notation per NOTATION.md

---

## Phase 3: Extraction & Consolidation

### Concept Card Structure

Each extracted concept becomes a structured "card":

```markdown
## Concept: [Name]

### Definition
[Precise, quotable definition from source. Preserve exact wording.]

**Source:** [Book/Author, Section/Page]

### Intuition  
[1-2 paragraph accessible explanation. What is this *really* about?]

### Key Examples
1. [Canonical example 1]
2. [Canonical example 2]
3. [Canonical example 3]

### Equivalent Characterizations
- [Alternative definition 1]
- [Alternative definition 2]

### Key Theorems
- **[Theorem Name]:** [Statement]
- **[Theorem Name]:** [Statement]

### Proof Techniques
- [Common proof strategy for results involving this concept]

### Common Errors / Gotchas
- [Misconception 1]
- [Misconception 2]

### Prerequisites
- [Concept this depends on]
- [Concept this depends on]

### Connections
- **Generalizes:** [simpler concept]
- **Specializes to:** [more specific concept]  
- **Related to:** [concept in same field]
- **Analogous to:** [concept in different field]

### Notation Variants
- [Alternative notation used by some authors]
```

### Extraction Prompt

See: `PROMPT-extraction.md` (to be created)

### Organizing Extracted Cards

```
extracted/
├── groups/
│   ├── group.md
│   ├── subgroup.md
│   ├── normal-subgroup.md
│   ├── quotient-group.md
│   ├── homomorphism.md
│   ├── isomorphism-theorems.md
│   ├── group-action.md
│   ├── sylow-theorems.md
│   └── ...
├── categories/
│   ├── category.md
│   ├── functor.md
│   ├── natural-transformation.md
│   ├── yoneda-lemma.md
│   ├── limit.md
│   ├── adjunction.md
│   ├── monad.md
│   └── ...
├── types/
│   ├── type.md
│   ├── dependent-product.md
│   ├── dependent-sum.md
│   ├── identity-type.md
│   ├── universe.md
│   └── ...
├── homotopy/
│   ├── homotopy.md
│   ├── fundamental-group.md
│   ├── higher-homotopy-groups.md
│   ├── fibration.md
│   ├── cofibration.md
│   ├── cw-complex.md
│   └── ...
└── hott/
    ├── univalence.md
    ├── higher-inductive-type.md
    ├── n-type.md
    ├── truncation.md
    └── ...
```

---

## Phase 3.5: Synthesis & Reconciliation

When multiple sources cover the same field, their extracted cards must be merged before guide generation.

### Why Synthesis is Necessary

Different sources may have:
- **Different definitions** (equivalent but worded differently)
- **Different notation** (even for the same concept)
- **Different examples** (complementary coverage)
- **Different scope** (one more general, one more specific)
- **Genuine disagreements** (conventions, edge cases)

### Synthesis Process

1. **Inventory:** List all concepts across all sources, noting coverage
2. **Classify differences:** Identical / Complementary / Notational / Equivalent / Disagreement
3. **Merge cards:** Produce ONE unified card per concept
4. **Document decisions:** Record how conflicts were resolved

### Unified Card Structure (Enhanced)

The unified card extends the extraction card with:

```markdown
## Concept: [Name]

### Definition
[Canonical definition — chosen for precision and usability]

**Source:** [Primary source]

**Alternative definitions:**
- [Source B]: [their version]
- [Source C]: [their version]

### Notation
**Standard (this skill):** [per NOTATION.md]

**Variants:**
| Notation | Used by | Notes |
|----------|---------|-------|

### Source Concordance
| Aspect | Source A | Source B | Source C |
|--------|----------|----------|----------|
| Definition | §X.Y | §A.B | [article] |
| Main theorem | Thm X.Y | Prop A.B | — |

[... rest of card structure ...]
```

### Handling Conflicts

| Conflict Type | Resolution |
|---------------|------------|
| Different notation | Standardize to NOTATION.md, list variants |
| Equivalent definitions | Pick clearest as primary, list others as equivalent characterizations |
| Different scope | Use scope appropriate for skill; note alternatives |
| Genuine disagreement | Document both positions, state which we adopt and why |

### Output Structure

```
synthesized/
├── [field]/
│   ├── _SYNTHESIS_NOTES.md    # Decisions, conflicts, exclusions
│   ├── [concept-1].md         # Unified card
│   ├── [concept-2].md
│   └── ...
```

### Extraction Prompt for Synthesis

See: `PROMPT-synthesis.md`

---

## Phase 4: Guide Generation

### Guide Structure

Each guide should be **2,000–4,000 tokens** (roughly 1,500–3,000 words).

```markdown
# [Topic] Guide

## Overview
[What this topic is about, why it matters, where it fits]

## Prerequisites
[What to read first, with links to other guides]

## Core Concepts
[Ordered presentation of the key ideas, building on each other]

### [Concept 1]
[Condensed from concept card — definition, intuition, key example]

### [Concept 2]
...

## Key Theorems
[The major results, with statements and proof sketches]

## Techniques
[How to work with these objects — common proof patterns]

## Examples
[Worked examples demonstrating the concepts]

## Connections
[How this topic relates to others in the skill]

## Further Reading
[Which source documents to consult for more depth]
```

### Guide Generation Prompt

See: `PROMPT-guide-generation.md` (to be created)

### Guide Organization

```
topics/
├── groups/
│   ├── GUIDE.md              # Overview of group theory
│   ├── basics.md             # Groups, subgroups, homomorphisms
│   ├── actions.md            # Group actions, orbits, stabilizers
│   ├── sylow.md              # Sylow theorems and applications
│   ├── representations.md    # Representation theory intro
│   └── lie-groups.md         # Lie groups and Lie algebras (intro)
│
├── categories/
│   ├── GUIDE.md              # Overview of category theory
│   ├── basics.md             # Categories, functors, natural transformations
│   ├── universals.md         # Universal properties, representables, Yoneda
│   ├── limits.md             # Limits and colimits
│   ├── adjunctions.md        # Adjunctions
│   ├── monads.md             # Monads and algebras
│   └── kan-extensions.md     # Kan extensions
│
├── types/
│   ├── GUIDE.md              # Overview of type theory
│   ├── basics.md             # Types, terms, judgments
│   ├── dependent-types.md    # Π and Σ types
│   ├── identity-types.md     # Identity, equality, paths
│   ├── inductive-types.md    # Inductive types and recursion
│   └── universes.md          # Universes and universe polymorphism
│
├── homotopy/
│   ├── GUIDE.md              # Overview of homotopy theory
│   ├── basics.md             # Homotopy, homotopy equivalence
│   ├── fundamental-group.md  # π₁ and covering spaces
│   ├── higher-groups.md      # Higher homotopy groups
│   ├── homology.md           # Homology and cohomology (intro)
│   └── model-categories.md   # Model categories (intro)
│
└── hott/
    ├── GUIDE.md              # Overview of HoTT
    ├── types-as-spaces.md    # The homotopy interpretation
    ├── univalence.md         # Univalence axiom
    ├── hits.md               # Higher inductive types
    └── synthetic.md          # Synthetic homotopy theory
```

### Connection Guides

```
connections/
├── cat-type.md               # Categories as models of type theory
├── cat-homotopy.md           # Categories and homotopy (∞-categories)
├── type-homotopy.md          # Identity types as paths
├── groups-groupoids.md       # Groups as one-object groupoids
├── univalence-explained.md   # Full treatment of univalence
└── rosetta-stone.md          # Parallel concepts across all four fields
```

---

## Phase 5: SKILL.md Assembly

### SKILL.md Structure

```markdown
# Higher Mathematics Skill

## Purpose
[What this skill enables]

## How to Use This Skill
[Instructions for Claude on when/how to consult these materials]

## Query Routing
[Decision tree for which documents to read based on user query]

## Document Map
[Complete listing of all guides and their contents]

## Working Style
[How to approach problems in these areas]

## Notation
[Link to NOTATION.md, key conventions]

## Sources
[Authoritative sources these materials derive from]
```

### Query Routing Logic

```markdown
## Query Routing

### By Keyword
| If query contains... | Consult... |
|---------------------|------------|
| group, subgroup, Sylow, coset | topics/groups/ |
| category, functor, natural transformation | topics/categories/ |
| type, Π, Σ, dependent, Agda, Coq | topics/types/ |
| homotopy, π₁, fibration, CW complex | topics/homotopy/ |
| univalence, HoTT, path, identity type | topics/hott/ |

### By Question Type
| Question type | Approach |
|--------------|----------|
| "What is X?" | Find concept card or guide section for X |
| "Prove that..." | Check relevant theorems, then proof techniques |
| "How does X relate to Y?" | Check connections/ guides |
| "Give an example of..." | Check examples in concept cards |
| "Why is X true?" | Find theorem statement, then proof sketch |

### Ambiguous Queries
If a concept appears in multiple fields (e.g., "product"), check context:
- Cartesian product (sets/categories) → categories/limits.md
- Product type (type theory) → types/dependent-types.md  
- Direct product (groups) → groups/basics.md
```

---

## Phase 6: Validation

### Test Problem Sets

Create 10–20 problems per area with known solutions.

#### Types of Problems

1. **Definition recall**: "State the definition of X"
2. **Example generation**: "Give an example of X with property Y"
3. **Proof exercises**: "Prove that X implies Y"
4. **Computation**: "Calculate π₁(X)" or "Find all groups of order n"
5. **Connection questions**: "Explain how X in field A relates to Y in field B"
6. **Error detection**: "Find the error in this proof"

#### Validation Process

1. Run each problem through Claude with only the skill documents available
2. Compare answers to known solutions
3. Note which problems fail and diagnose:
   - Missing content?
   - Poorly organized content?
   - Routing failure?
4. Iterate on skill documents until pass rate is acceptable

### Validation Checklist

- [ ] All core definitions are correctly stated
- [ ] Major theorems have correct statements
- [ ] Proof sketches lead to valid proofs
- [ ] Examples are correctly computed
- [ ] Cross-field connections are accurately described
- [ ] No circular dependencies in prerequisites
- [ ] Notation is consistent throughout

---

## File Structure Summary

```
/mnt/skills/user/higher-maths/
│
├── SKILL.md                    # Entry point
├── OVERVIEW.md                 # Conceptual map of all four fields
├── PREREQUISITES.md            # Background needed
├── NOTATION.md                 # Notation conventions
│
├── prompts/
│   ├── PROMPT-extraction.md    # Prompt for Phase 3
│   ├── PROMPT-synthesis.md     # Prompt for Phase 3.5
│   ├── PROMPT-guide-gen.md     # Prompt for Phase 4
│   └── PROMPT-skill-assembly.md # Prompt for Phase 5
│
├── sources/                    # Converted original sources
│   ├── versions.md             # Source versioning info
│   ├── milne-groups/
│   ├── judson-algebra/
│   ├── riehl-context/
│   ├── leinster-basic/
│   ├── hatcher-topology/
│   ├── hott-book/
│   ├── martin-lof/
│   ├── plfa/
│   └── nlab/
│
├── extracted/                  # Concept cards (per source)
│   ├── groups/
│   │   ├── milne/
│   │   └── judson/
│   ├── categories/
│   │   ├── riehl/
│   │   ├── leinster/
│   │   └── nlab/
│   ├── types/
│   ├── homotopy/
│   └── hott/
│
├── synthesized/                # Unified concept cards (one per concept)
│   ├── groups/
│   │   └── _SYNTHESIS_NOTES.md
│   ├── categories/
│   │   └── _SYNTHESIS_NOTES.md
│   ├── types/
│   ├── homotopy/
│   └── hott/
│
├── topics/                     # Final guides (built from synthesized cards)
│   ├── groups/
│   ├── categories/
│   ├── types/
│   ├── homotopy/
│   └── hott/
│
├── connections/                # Cross-field guides
│
├── examples/                   # Worked problems
│   └── worked/
│
└── validation/                 # Test problems
    ├── groups-problems.md
    ├── categories-problems.md
    ├── types-problems.md
    ├── homotopy-problems.md
    └── solutions/              # (kept separate to avoid contamination)
```

---

## Timeline Estimate

| Phase | Effort | Notes |
|-------|--------|-------|
| 1. Source acquisition | 1-2 days | Downloading, organizing |
| 2. Conversion | 3-5 days | Depends heavily on PDF quality |
| 3. Extraction | 5-10 days | ~50-100 concepts per field, per source |
| 3.5. Synthesis | 2-4 days | Merging cards, resolving conflicts |
| 4. Guide generation | 3-5 days | ~5-8 guides per field |
| 5. SKILL.md assembly | 1 day | |
| 6. Validation | 2-3 days | Iterative |

**Total: 3-5 weeks** depending on depth and iteration cycles.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2025-01-23 | Initial workflow draft |
| 0.2 | 2025-01-23 | Added Phase 3.5 Synthesis |
