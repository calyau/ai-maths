# Guide Generation Prompt for Higher Mathematics

## Purpose

This prompt synthesizes extracted concept cards into cohesive, AI-optimized guides. Each guide covers a coherent subtopic and is sized for effective retrieval and reasoning (2,000–4,000 tokens).

---

## The Prompt

```
You are synthesizing mathematical concept cards into a cohesive guide document. Your goal is to create a clear, well-structured reference that enables accurate mathematical reasoning and problem-solving.

## Guide Metadata

**Guide Title:** [TITLE]
**Field:** [GROUP THEORY | TYPE THEORY | CATEGORY THEORY | HOMOTOPY THEORY | HOTT]
**Subtopic:** [SUBTOPIC]
**Target Length:** 2,000–4,000 tokens (approximately 1,500–3,000 words)

## Input: Concept Cards

<concept_cards>
[PASTE RELEVANT CONCEPT CARDS HERE]
</concept_cards>

## Guide Structure

Generate a guide following this structure:

---

# [Subtopic]: [Descriptive Title]

## Overview

[2-3 paragraphs providing:]
- What this subtopic is about
- Why it matters / what problems it solves
- How it fits into the broader field
- What you'll be able to do after understanding this material

## Prerequisites

[Bulleted list of concepts/guides that should be understood first. Be minimal — list direct prerequisites only, not transitive ones.]

- **[Concept/Guide]** — [one-line description of why it's needed]
- **[Concept/Guide]** — [one-line description of why it's needed]

**Notation:** This guide uses notation from `NOTATION.md`. Key symbols:
- [symbol] — [meaning]
- [symbol] — [meaning]

---

## Core Concepts

[Present concepts in logical order, building from simpler to more complex. Each concept should flow naturally into the next.]

### [Concept 1 Name]

**Definition.** [Precise definition — quote from concept card]

[1-2 paragraphs of explanation/intuition]

**Example.** [One concrete, worked example]

[Additional brief examples if useful, as a bulleted list]

---

### [Concept 2 Name]

**Definition.** [Precise definition]

[Explanation building on Concept 1]

**Example.** [Concrete example, ideally showing relationship to Concept 1]

---

[Continue for all core concepts...]

---

## Key Results

[Present the major theorems, organized logically]

### [Theorem Name]

**Theorem.** [Precise statement]

**Significance.** [Why this theorem matters — what does it let you do?]

**Proof sketch.** [Key ideas of the proof in 2-5 sentences. Not a full proof, but enough to remember the structure.]

**Application.** [One concrete application or corollary]

---

### [Next Theorem...]

---

## Proof Techniques

[Practical guidance for working in this area]

### How to Prove [Type of Statement]

1. [Step or strategy]
2. [Step or strategy]
3. [Step or strategy]

**Watch out for:** [Common pitfall]

### How to Prove [Another Type of Statement]

[...]

---

## Worked Examples

[2-3 complete worked examples demonstrating the concepts and techniques]

### Example 1: [Descriptive Title]

**Problem.** [Clear statement]

**Solution.**

[Step-by-step solution with justification for each step. Reference which definitions/theorems are being used.]

---

### Example 2: [Descriptive Title]

**Problem.** [Clear statement]

**Solution.**

[...]

---

## Common Errors

[Bulleted list of mistakes to avoid]

- **[Error type]:** [Description of the error and why it's wrong]
  - *Correct approach:* [What to do instead]

- **[Error type]:** [...]

---

## Connections

### Within [Current Field]

- **[Related subtopic]:** [How this material connects — e.g., "Adjunctions generalize to..." or "This is a special case of..."]

### To Other Fields

- **[Other field]:** [Specific connection — not vague hand-waving but concrete correspondence]

[Only include genuine, useful connections. It's fine to omit a field if there's no natural connection at this level.]

---

## Summary

[Concise summary of the key takeaways — what someone should remember]

**Key definitions:**
- [Concept]: [One-line summary]
- [Concept]: [One-line summary]

**Key results:**
- [Theorem]: [One-line summary of what it says]
- [Theorem]: [One-line summary]

**Key techniques:**
- To [accomplish X], use [technique Y]

---

## Further Reading

[Pointers to more depth]

- **For more detail:** [Source document(s) in the skill]
- **For advanced topics:** [What to explore next]
- **Original sources:** [Key references from the literature]

---

## Generation Guidelines

### Sizing

- **Target:** 2,000–4,000 tokens
- **If over:** Split into multiple guides by subtopic
- **If under:** You may be missing important concepts or examples — check the cards

### Ordering Principles

1. **Dependency order:** Never use a concept before defining it
2. **Concrete before abstract:** Start with examples, then generalize
3. **Simple before complex:** Build up gradually
4. **Motivation before definition:** Say why we care, then give the formal definition

### Voice and Style

- **Precise but accessible:** Definitions must be exact; explanations should build intuition
- **Active voice:** "We define..." rather than "It is defined that..."
- **Direct:** "This means..." rather than "It can be seen that this implies..."
- **Confident but honest:** State what's true clearly; acknowledge genuine subtleties

### Mathematical Writing

- **Definitions:** Use "Definition." in bold, then the precise statement
- **Theorems:** Use "Theorem." in bold (or Lemma/Proposition/Corollary as appropriate)
- **Proofs:** Use "Proof." or "Proof sketch." — always indicate when a proof ends
- **Examples:** Use "Example." in bold, make them concrete and computable

### What to Include

✓ Every core definition from the input cards
✓ The most important theorems (not every lemma)
✓ Concrete, worked examples
✓ Proof sketches for major results
✓ Common errors and how to avoid them
✓ Genuine connections to other topics

### What to Exclude

✗ Long, detailed proofs (reference the source instead)
✗ Exhaustive lists of minor results
✗ Vague or forced connections
✗ Historical digressions (unless directly illuminating)
✗ Exercises without solutions (this is a reference, not a problem set)

### Handling Difficulty

- **If a concept is hard:** Give more examples, break it into steps
- **If a proof is complex:** Give the key insight, reference full proof
- **If notation is heavy:** Introduce incrementally, provide a notation table

---

## Quality Checklist

Before finalizing the guide:

- [ ] **Complete:** All core concepts from input cards are covered
- [ ] **Ordered:** No forward references to undefined concepts
- [ ] **Precise:** Definitions and theorem statements are exact
- [ ] **Concrete:** Every abstract concept has at least one concrete example
- [ ] **Correct:** Mathematical content is accurate
- [ ] **Connected:** Links to prerequisites and related topics are included
- [ ] **Sized:** Within 2,000–4,000 token target
- [ ] **Standalone:** Guide is self-contained given stated prerequisites
- [ ] **Actionable:** Reader knows how to use/prove things, not just what they are

---

## Example: Partial Guide Output

Here's an example of what part of a generated guide should look like:

---

# Adjunctions: The Universal Translator

## Overview

Adjunctions are perhaps the most important concept in category theory after categories themselves. They capture a precise sense in which two functors are "optimally related" — one freely generates structure, the other forgets it, and the two processes are perfectly matched.

Nearly every important construction in mathematics can be viewed as an adjunction: free groups, tensor products, limits and colimits, Stone-Čech compactification, and many more. Understanding adjunctions means understanding *why* these constructions exist and what universal properties they satisfy.

After this guide, you'll be able to: recognize adjunctions in the wild, verify that two functors form an adjoint pair, apply the fact that right adjoints preserve limits, and see how adjunctions generate monads.

## Prerequisites

- **Functors** — we need to compose and compare functors
- **Natural transformations** — adjunctions involve natural isomorphisms
- **Hom-sets** — the definition involves Hom(F(X), Y) ≅ Hom(X, G(Y))
- **Limits** (optional) — needed for the RAPL theorem, but not for basic definitions

**Notation:**
- F : C → D denotes a functor from category C to category D
- Hom_C(X, Y) is the set of morphisms from X to Y in category C
- ≅ denotes isomorphism (of sets, when applied to Hom-sets)
- F ⊣ G means F is left adjoint to G

---

## Core Concepts

### Adjunction

**Definition.** Let F : C → D and G : D → C be functors. An **adjunction** F ⊣ G consists of a natural isomorphism

φ : Hom_D(F(X), Y) ≅ Hom_C(X, G(Y))

for all objects X in C and Y in D. We call F the **left adjoint** and G the **right adjoint**.

The naturality means: for any morphisms f : X' → X in C and g : Y → Y' in D, the following diagram commutes:

```
Hom_D(F(X), Y) ----φ----> Hom_C(X, G(Y))
      |                        |
      | (Ff)* and g*           | f* and (Gg)*
      v                        v
Hom_D(F(X'), Y') --φ---> Hom_C(X', G(Y'))
```

Think of it this way: F and G provide a "dictionary" between C and D. The adjunction says this dictionary is perfectly consistent — translating a map one way and then back doesn't lose information.

**Example.** The paradigmatic example: Let F : Set → Grp be the free group functor and U : Grp → Set the forgetful functor. Then F ⊣ U.

Concretely: a group homomorphism F(S) → G (from the free group on set S to a group G) is completely determined by where the generators go. That's exactly a function S → U(G). The adjunction isomorphism is:

Hom_Grp(F(S), G) ≅ Hom_Set(S, U(G))

This isn't just a bijection — it's natural, meaning it respects composition with other homomorphisms and functions.

---

### Unit and Counit

**Definition.** Given an adjunction F ⊣ G, the **unit** is a natural transformation

η : 1_C → GF

and the **counit** is a natural transformation

ε : FG → 1_D

These satisfy the **triangle identities:**

(εF) ∘ (Fη) = 1_F    and    (Gε) ∘ (ηG) = 1_G

The unit η_X : X → GF(X) is the "universal map into something in the image of G." The counit ε_Y : FG(Y) → Y is the "universal map out of something in the image of F."

**Example.** For the free group adjunction F ⊣ U:

- The unit η_S : S → UF(S) sends each element s ∈ S to itself, viewed as a generator in the free group F(S). This is the "insertion of generators."

- The counit ε_G : FU(G) → G takes the free group on the underlying set of G and maps it to G by "evaluating" — each generator (which is an element of G) maps to itself.

---

[Guide continues with Key Results, Proof Techniques, Worked Examples, etc.]

---

Now generate the complete guide from the concept cards provided above.
```

---

## Prompt Variants

### Variant A: Overview Guide

For generating the top-level `GUIDE.md` that introduces an entire field:

```
[Use base prompt above, but replace the Guide Structure section with:]

## Guide Structure for Field Overview

Generate an overview guide with:

1. **What is [Field]?** — Accessible introduction
2. **Why study [Field]?** — Motivation and applications  
3. **Core ideas in one page** — The 3-5 most essential concepts
4. **Map of the territory** — How subtopics relate to each other
5. **Learning path** — Suggested order for the detailed guides
6. **Connections to other fields** — Where [Field] touches the other three areas

Target length: 2,000–3,000 tokens. This should be readable by someone new to the field.
```

### Variant B: Connections Guide

For generating cross-field connection documents:

```
[Use base prompt above, but replace the Guide Structure section with:]

## Guide Structure for Connections

Generate a connections guide with:

1. **The Correspondence** — What concepts in Field A correspond to what in Field B?
2. **Precise Statements** — Formal theorems relating the two
3. **Dictionary** — Table mapping terminology between fields
4. **Examples** — Show the same mathematical object from both perspectives
5. **Why It Matters** — What does this connection let you do?
6. **Limitations** — Where does the analogy break down?

Be precise about what is a theorem vs. what is an informal analogy.
```

### Variant C: Techniques Guide

For generating "how to prove things" practical guides:

```
[Use base prompt above, but replace Core Concepts/Key Results with:]

## Guide Structure for Techniques

1. **Standard Proof Strategies** — The go-to approaches
2. **When to Use What** — Decision tree for choosing techniques
3. **Detailed Walkthroughs** — Step-by-step examples of each technique
4. **Troubleshooting** — What to try when you're stuck
5. **Templates** — Fill-in-the-blank proof outlines

Focus on practical, actionable guidance over theory.
```

---

## Chunking Guidelines

### When to Split a Guide

Split into multiple guides if:
- Token count exceeds 4,500
- There's a natural conceptual break (e.g., "basic" vs "advanced")
- Prerequisites diverge (some readers need Part A but not Part B)

### How to Split

1. **By difficulty:** `basics.md`, `intermediate.md`, `advanced.md`
2. **By subarea:** `limits.md`, `colimits.md` (rather than one huge `limits-and-colimits.md`)
3. **By application:** `sylow-theorems.md`, `sylow-applications.md`

### Naming Conventions

```
[topic].md           — Main guide for a topic
[topic]-basics.md    — Introductory material
[topic]-advanced.md  — Advanced material
[topic]-techniques.md — How-to guide
[topic]-examples.md  — Extended worked examples
```

---

## Post-Processing Checklist

After generating guides:

- [ ] Verify all internal links point to existing files
- [ ] Check that prerequisite chains are acyclic
- [ ] Ensure notation is consistent with NOTATION.md
- [ ] Validate mathematical correctness (spot-check theorems)
- [ ] Test readability: can you follow without the concept cards?
- [ ] Confirm token count is in range

---

## Integration with SKILL.md

Each generated guide should be registered in SKILL.md's routing table:

```markdown
## Document Index

### Category Theory
| Guide | Covers | Prerequisites |
|-------|--------|---------------|
| `categories/GUIDE.md` | Field overview | None |
| `categories/basics.md` | Categories, functors, natural transformations | GUIDE |
| `categories/yoneda.md` | Yoneda lemma, representables | basics |
| `categories/limits.md` | Limits and colimits | basics |
| `categories/adjunctions.md` | Adjunctions | limits |
| `categories/monads.md` | Monads and algebras | adjunctions |
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-23 | Initial prompt |
