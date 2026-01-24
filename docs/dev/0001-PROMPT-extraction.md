# Extraction Prompt for Higher Mathematics Sources

## Purpose

This prompt is used to process converted source materials (textbooks, lecture notes, wiki articles) and extract structured "concept cards" suitable for AI consumption and mathematical reasoning.

---

## The Prompt

```
You are extracting structured mathematical knowledge from a source document to build a reference system for higher mathematics. Your goal is to create precise, well-organized "concept cards" that capture definitions, theorems, examples, and connections.

## Source Information

**Source Title:** [TITLE]
**Author(s):** [AUTHORS]  
**Section/Chapter:** [SECTION]
**Field:** [GROUP THEORY | TYPE THEORY | CATEGORY THEORY | HOMOTOPY THEORY | HOTT]

## Input

<source_material>
[PASTE CONVERTED SOURCE TEXT HERE]
</source_material>

## Extraction Instructions

### 1. Identify All Concepts

List every mathematical concept that is **defined or substantially discussed** in this source material. Include:
- Definitions (explicit "Definition X.Y" statements)
- Named theorems, lemmas, propositions, corollaries
- Key constructions (e.g., "the free group on a set")
- Important examples that illustrate general principles

### 2. For Each Concept, Create a Card

Use the following structure. **Preserve precision in definitions and theorem statements** — quote directly when possible rather than paraphrasing.

---

## Concept: [Concept Name]

### Definition

[The precise mathematical definition. Use exact wording from the source. If multiple equivalent definitions exist, give the primary one here and list alternatives below.]

**Source:** [Book Title, Theorem/Definition number, page if available]

### Notation

[Standard notation for this concept, following the project's NOTATION.md conventions]

### Intuition

[A 1-2 paragraph explanation in accessible terms. What is this concept *really* about? Why does it exist? What problem does it solve?]

### Key Examples

[List 2-5 canonical examples. These should be the examples that every mathematician knows and uses to build intuition.]

1. **[Example name]:** [Brief description]
2. **[Example name]:** [Brief description]
3. ...

### Non-Examples / Counterexamples

[If applicable, give examples of things that are NOT instances of this concept but might be confused for it]

### Equivalent Characterizations

[Alternative definitions or ways of characterizing the same concept. Note which source each comes from if they differ.]

- [Alternative 1]
- [Alternative 2]

### Key Theorems Involving This Concept

[State theorems precisely. Include proof sketches only if they're short and illuminating.]

**Theorem ([Name/Number]):** [Precise statement]

*Proof sketch:* [Brief outline of proof strategy, if available and useful]

### Proof Techniques

[What are the standard ways to prove things about this concept? What tools does one typically reach for?]

### Common Errors / Gotchas

[Misconceptions, easy mistakes, subtle points that trip people up]

- [Error 1]: [Why it's wrong and what's correct]
- [Error 2]: ...

### Prerequisites

[What concepts must be understood before this one? List as links to other concept cards.]

- [Prerequisite concept 1]
- [Prerequisite concept 2]

### Leads To

[What concepts build on this one?]

- [Downstream concept 1]
- [Downstream concept 2]

### Connections to Other Fields

[How does this concept appear in or relate to the other three fields in our scope?]

- **Group Theory:** [Connection, if any]
- **Category Theory:** [Connection, if any]
- **Type Theory:** [Connection, if any]
- **Homotopy Theory:** [Connection, if any]

### Notation Variants

[Different notation used by different authors/traditions]

| Notation | Used by | Notes |
|----------|---------|-------|
| [variant] | [author/tradition] | [when to use] |

### Computation / Algorithms

[If applicable: how does one actually compute with this concept? Any algorithms?]

### Open Questions / Advanced Topics

[If the source mentions open problems or advanced generalizations, note them briefly]

---

## 3. Quality Checks

Before finalizing each card, verify:

- [ ] **Definition is precise:** Could someone unfamiliar reconstruct the exact meaning?
- [ ] **Definition is quoted, not paraphrased** (when possible)
- [ ] **Examples are concrete:** Not just "e.g., any group" but specific groups
- [ ] **Prerequisites are minimal:** Don't list prerequisites of prerequisites
- [ ] **Connections are accurate:** Don't force connections that don't exist
- [ ] **Notation matches NOTATION.md:** Convert if necessary
- [ ] **No orphan concepts:** Everything links to something else

## 4. Output Format

Produce one markdown file per concept, named in lowercase-with-hyphens:
- `group.md`
- `normal-subgroup.md`  
- `yoneda-lemma.md`
- `dependent-product-type.md`

At the end, produce an index file listing all extracted concepts with one-line descriptions.

## 5. Handling Edge Cases

### Ambiguous Concepts
If a term means different things in different contexts (e.g., "product"), create separate cards:
- `product-category-theory.md`
- `product-type-theory.md`
- `direct-product-groups.md`

And create a disambiguation note at the top of each.

### Concepts Without Full Definitions
If the source uses but doesn't define a concept, note this:
> **Note:** This source uses but does not define [concept]. See [other source] for definition.

### Very Long Proofs
Don't reproduce long proofs in full. Instead:
- State the theorem precisely
- Give proof sketch (key ideas, structure)
- Note "Full proof: [Source], pp. X-Y"

### Diagrams
If the source contains essential diagrams:
- Describe the diagram in text
- Note: "See [Source], Figure X.Y for diagram"
- If possible, recreate as ASCII art for simple commutative diagrams:

```
      F
  A -----> B
  |        |
G |        | H
  |        |
  v        v
  C -----> D
      K
```

## 6. Special Instructions by Field

### Group Theory
- Always note whether a result applies to all groups, finite groups, or abelian groups
- For named groups (S_n, A_n, GL_n, etc.), include standard notation and basic properties
- Note connections to representation theory where applicable

### Category Theory  
- Always note size issues (small, locally small, large categories)
- For universal properties, state both the object and the universal morphism
- Include the relevant diagrams (as ASCII art if simple)

### Type Theory
- Distinguish formation rules, introduction rules, elimination rules, computation rules
- Note whether results depend on extensionality, univalence, or other axioms
- Be precise about contexts (Γ ⊢ ...)

### Homotopy Theory / HoTT
- Note whether spaces are assumed to be CW complexes, locally compact, etc.
- For HoTT, note h-level (contractible, prop, set, n-type)
- Distinguish point-set topology from homotopy-theoretic properties

---

## Example Card

Here's a complete example to illustrate the format:

---

## Concept: Adjunction

### Definition

Let C and D be categories. An **adjunction** between C and D consists of:
- A functor F : C → D (the **left adjoint**)
- A functor G : D → C (the **right adjoint**)  
- A natural isomorphism Hom_D(F(X), Y) ≅ Hom_C(X, G(Y)) for all X in C and Y in D

We write F ⊣ G and say "F is left adjoint to G" or "G is right adjoint to F."

**Source:** Riehl, *Category Theory in Context*, Definition 4.1.1

### Notation

- F ⊣ G — F is left adjoint to G
- The natural isomorphism is often denoted φ : Hom_D(F-, -) ≅ Hom_C(-, G-)

### Intuition

An adjunction captures the idea of "best approximation" or "free construction." The left adjoint F freely generates D-structure from C-objects, while the right adjoint G forgets D-structure to get a C-object. The adjunction says: a map from "freely generated" to Y is the same data as a map from the original to "underlying structure of Y."

Think of it as an efficient translation between two mathematical languages where you lose no information going back and forth.

### Key Examples

1. **Free-Forgetful (Groups):** The free group functor F : Set → Grp is left adjoint to the forgetful functor U : Grp → Set. A group homomorphism F(S) → G is determined by where the generators go, i.e., a function S → U(G).

2. **Product-Hom (Currying):** For a fixed object A, the functor (- × A) is left adjoint to the functor Hom(A, -). This is currying: maps X × A → Y correspond to maps X → Y^A.

3. **Geometric Realization-Singular:** |−| : sSet → Top is left adjoint to Sing : Top → sSet.

4. **Discrete-Forgetful-Indiscrete:** For U : Top → Set, both the discrete topology functor and indiscrete topology functor are adjoints: Discrete ⊣ U ⊣ Indiscrete.

### Equivalent Characterizations

An adjunction F ⊣ G can equivalently be specified by:

1. **Hom-set bijection** (as above)
2. **Unit and counit:** Natural transformations η : 1_C → GF and ε : FG → 1_D satisfying triangle identities
3. **Universal arrows:** For each X in C, a universal arrow from X to G; or for each Y in D, a universal arrow from F to Y

### Key Theorems Involving This Concept

**Theorem (RAPL):** Right adjoints preserve limits.

*Proof sketch:* Use the Hom-set characterization and the fact that Hom(X, lim Y_i) ≅ lim Hom(X, Y_i).

**Theorem:** Every adjunction F ⊣ G gives rise to a monad GF on C and a comonad FG on D.

**Theorem (Adjoint Functor Theorems):** Under suitable conditions (solution set condition, etc.), a functor that preserves limits has a left adjoint.

### Proof Techniques

- To show F ⊣ G, often easiest to construct unit and counit and verify triangle identities
- To show a functor has an adjoint, apply adjoint functor theorem if conditions met
- To use an adjunction, apply RAPL/LAPL to move limits/colimits across

### Common Errors / Gotchas

- **Confusing left and right:** Left adjoint is the "free" one (F), right adjoint "forgets" (G). Mnemonic: "Free is left" (both have 4 letters starting with f/l... or just: Limit preservation is on the Right)
- **Forgetting naturality:** The Hom-set bijection must be natural in both arguments
- **Unit vs counit direction:** η : 1 → GF (unit inserts into free-then-forget), ε : FG → 1 (counit evaluates forget-then-free)

### Prerequisites

- [Functor]
- [Natural transformation]
- [Hom-set]
- [Limit] (for RAPL)

### Leads To

- [Monad] (every adjunction generates a monad)
- [Kan extension] (adjoints are Kan extensions along identity)
- [Equivalence of categories] (equivalences are adjunctions with invertible unit/counit)

### Connections to Other Fields

- **Group Theory:** Free group construction is the paradigmatic example
- **Type Theory:** Π and Σ types are adjoints to context extension/weakening
- **Homotopy Theory:** Quillen adjunctions between model categories induce adjunctions on homotopy categories

### Notation Variants

| Notation | Used by | Notes |
|----------|---------|-------|
| F ⊣ G | Standard | F left, G right |
| F ⊢ G | Some older texts | Reversed from modern convention! |
| (F, G, φ) | Explicit form | When bijection needs naming |

---

Now extract all concepts from the source material provided above, following this format.
```

---

## Usage Notes

### Before Running the Prompt

1. Convert source material to clean markdown
2. Ensure notation is normalized per NOTATION.md
3. Chunk large sources into manageable sections (one chapter at a time)

### After Running the Prompt

1. Review output for accuracy (especially theorem statements)
2. Check that examples are correctly attributed
3. Verify prerequisite chains don't have cycles
4. Cross-reference with other sources for completeness

### Iteration

Run multiple passes if needed:
- **First pass:** Extract all concepts mentioned
- **Second pass:** Fill in gaps, add connections
- **Third pass:** Verify accuracy against original source

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-23 | Initial prompt |
