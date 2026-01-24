# SKILL.md Generation Prompt

## Purpose

This prompt guides the final assembly of the SKILL.md file — the entry point that Claude reads first when the skill is activated. The SKILL.md must efficiently route Claude to the right documents and provide working instructions for mathematical assistance.

---

## Context: What is SKILL.md?

The SKILL.md file is:
- **The entry point** — Claude reads this first when the skill is loaded
- **A router** — It directs Claude to the appropriate detailed documents
- **An instruction manual** — It tells Claude *how* to use the skill materials
- **A map** — It provides an overview of what's available

The SKILL.md is NOT:
- A comprehensive reference (that's what the guides are for)
- A place for detailed mathematical content
- A substitute for reading the actual guides

**Critical constraint:** SKILL.md should be **under 4,000 tokens** — long enough to be useful, short enough to always fit in context alongside other materials.

---

## The Prompt

```
You are assembling the final SKILL.md file for a higher mathematics knowledge base. This file serves as Claude's entry point and routing guide for the skill.

## Available Materials

You have access to the following completed materials:

### Field Overviews
<field_overviews>
[LIST THE GUIDE.md FILES FOR EACH FIELD WITH ONE-LINE DESCRIPTIONS]
</field_overviews>

### Topic Guides
<topic_guides>
[LIST ALL TOPIC GUIDES ORGANIZED BY FIELD]
</topic_guides>

### Connection Guides  
<connection_guides>
[LIST ALL CROSS-FIELD CONNECTION DOCUMENTS]
</connection_guides>

### Reference Documents
<reference_docs>
- NOTATION.md — Standard notation conventions
- PREREQUISITES.md — Background knowledge requirements
- [Any other reference docs]
</reference_docs>

## Generation Task

Generate a SKILL.md file following the template below. Fill in all placeholders marked with [BRACKETS] and expand sections marked with {{EXPAND}}.

---

# TEMPLATE BEGINS HERE
---

# Higher Mathematics Skill

## Purpose

This skill enables Claude to assist with **Group Theory**, **Type Theory**, **Category Theory**, and **Homotopy Theory** (including Homotopy Type Theory). These four fields are deeply interconnected in modern mathematics, converging especially in HoTT.

**This skill provides:**
- Precise definitions and theorem statements
- Proof techniques and strategies  
- Worked examples
- Connections between fields
- Guidance on common errors to avoid

**This skill does NOT provide:**
- Exhaustive coverage of all results (consult original sources for that)
- Research-level material beyond standard graduate curriculum
- Computational tools (though it can explain algorithms)

---

## How to Use This Skill

### When to Consult These Materials

**ALWAYS read relevant guides when:**
- User asks for a definition, theorem statement, or proof
- User is working through a proof and needs verification
- User asks how concepts in different fields relate
- User is confused about notation or conventions

**You may answer directly (without consulting guides) when:**
- Giving high-level intuition or motivation
- The question is clearly outside the scope of these four fields
- Providing encouragement or structuring a study plan

### Reading Strategy

1. **Start with routing** (below) to identify which documents are relevant
2. **Read the field GUIDE.md first** if user is new to the area
3. **Read specific topic guides** for detailed work
4. **Check NOTATION.md** if there's any notational confusion
5. **Consult connection guides** when relating concepts across fields

### Working Style

When helping with mathematics from these fields:

1. **State what we're proving/computing and the strategy** before diving in
2. **Cite definitions and theorems by name** — e.g., "By the Yoneda lemma..."
3. **Be precise with quantifiers and hypotheses** — math is exact
4. **Flag where intuition might mislead** — note common errors
5. **Offer to explain more** if a step might be unclear
6. **Suggest related concepts** the user might want to explore

### When You're Uncertain

- **If a definition seems off:** Check the relevant guide; definitions must be exact
- **If you're not sure a theorem applies:** State your uncertainty explicitly
- **If asked about something not in the guides:** Say so, and offer to reason carefully from first principles (with appropriate caveats)

---

## Query Routing

Use this section to quickly identify which documents to consult.

### By Keyword

| Keywords in query | Primary document(s) |
|-------------------|---------------------|
| group, subgroup, coset, normal, quotient group, Sylow, order (of element/group) | `topics/groups/` |
| ring, field, module, ideal, polynomial | Outside core scope — answer from general knowledge |
| category, functor, natural transformation, diagram, commute | `topics/categories/` |
| limit, colimit, pullback, pushout, product, coproduct, terminal, initial | `topics/categories/limits.md` |
| adjoint, adjunction, free, forgetful, RAPL | `topics/categories/adjunctions.md` |
| monad, algebra over a monad, Kleisli, Eilenberg-Moore | `topics/categories/monads.md` |
| Yoneda, representable, presheaf | `topics/categories/yoneda.md` |
| type, term, judgment, context, Γ ⊢ | `topics/types/` |
| Π-type, dependent product, function type | `topics/types/dependent-types.md` |
| Σ-type, dependent sum, dependent pair | `topics/types/dependent-types.md` |
| identity type, Id, path, equality, propositional equality | `topics/types/identity-types.md` or `topics/hott/` |
| universe, Type, 𝒰, hierarchy | `topics/types/universes.md` |
| inductive type, W-type, recursion, induction principle | `topics/types/inductive-types.md` |
| Agda, Coq, Lean, proof assistant | `topics/types/` (and external documentation) |
| homotopy, homotopic, deformation, path (topological) | `topics/homotopy/` |
| fundamental group, π₁, loop, covering space | `topics/homotopy/fundamental-group.md` |
| higher homotopy, π_n, homotopy group | `topics/homotopy/higher-groups.md` |
| fibration, cofibration, lifting, extension | `topics/homotopy/fibrations.md` |
| CW complex, cell, attachment | `topics/homotopy/` |
| homology, cohomology, chain, cycle, boundary | `topics/homotopy/homology.md` |
| model category, weak equivalence, Quillen | `topics/homotopy/model-categories.md` |
| univalence, univalent, UA | `topics/hott/univalence.md` |
| HoTT, homotopy type theory | `topics/hott/GUIDE.md` |
| higher inductive type, HIT, circle type, truncation | `topics/hott/hits.md` |
| n-type, h-level, set, prop, contractible | `topics/hott/n-types.md` |
| path induction, J eliminator, based path induction | `topics/hott/` or `topics/types/identity-types.md` |

### By Question Type

| Question pattern | Approach |
|------------------|----------|
| "What is [X]?" / "Define [X]" | Find X in topic guides → give precise definition + intuition |
| "Prove that..." / "Show that..." | Identify relevant theorems → outline proof strategy → execute |
| "Why is [X] true?" | Find theorem → provide proof sketch or key insight |
| "How does [X] relate to [Y]?" | Check connection guides if X,Y in different fields; otherwise check both topic guides |
| "Give an example of..." | Find concept → provide canonical example from guide |
| "Is it true that...?" | Carefully check — might be true, false, or dependent on axioms |
| "What's the intuition for...?" | Give conceptual explanation, but ground it in the precise definition |
| "I'm confused about..." | Identify the confusion → clarify with definition + example + common errors |

### Ambiguous Terms

Some terms mean different things in different contexts:

| Term | Possibilities | How to disambiguate |
|------|---------------|---------------------|
| "product" | Cartesian product (Set), categorical product, product type, direct product (groups) | Ask context or infer from surrounding terms |
| "path" | Topological path, identity type term (HoTT), path in a graph | "path" + type theory context → identity type |
| "equivalence" | Equivalence relation, equivalence of categories, homotopy equivalence, type equivalence | Context usually clear; ask if not |
| "isomorphism" | Group iso, category iso, type iso (≃), homeomorphism | Determined by the objects being compared |
| "function" | Set function, morphism, term of function type | Usually clear from context |
| "element" | Set element, term of a type, object of a category (informally) | Type theory → "term"; category theory → "object" |
| "natural" | Natural transformation, natural numbers, "natural" (colloquial) | Category theory context → natural transformation |

---

## Document Map

### Overview & Reference

| Document | Purpose |
|----------|---------|
| `OVERVIEW.md` | Conceptual map of all four fields and their connections |
| `PREREQUISITES.md` | What background is assumed |
| `NOTATION.md` | Standard notation used throughout |

### Group Theory

| Document | Covers |
|----------|--------|
| `topics/groups/GUIDE.md` | [ONE-LINE DESCRIPTION] |
| `topics/groups/basics.md` | [ONE-LINE DESCRIPTION] |
| `topics/groups/actions.md` | [ONE-LINE DESCRIPTION] |
| `topics/groups/sylow.md` | [ONE-LINE DESCRIPTION] |
{{EXPAND: List all group theory guides}}

### Category Theory

| Document | Covers |
|----------|--------|
| `topics/categories/GUIDE.md` | [ONE-LINE DESCRIPTION] |
| `topics/categories/basics.md` | [ONE-LINE DESCRIPTION] |
| `topics/categories/yoneda.md` | [ONE-LINE DESCRIPTION] |
| `topics/categories/limits.md` | [ONE-LINE DESCRIPTION] |
| `topics/categories/adjunctions.md` | [ONE-LINE DESCRIPTION] |
| `topics/categories/monads.md` | [ONE-LINE DESCRIPTION] |
{{EXPAND: List all category theory guides}}

### Type Theory

| Document | Covers |
|----------|--------|
| `topics/types/GUIDE.md` | [ONE-LINE DESCRIPTION] |
| `topics/types/basics.md` | [ONE-LINE DESCRIPTION] |
| `topics/types/dependent-types.md` | [ONE-LINE DESCRIPTION] |
| `topics/types/identity-types.md` | [ONE-LINE DESCRIPTION] |
| `topics/types/inductive-types.md` | [ONE-LINE DESCRIPTION] |
| `topics/types/universes.md` | [ONE-LINE DESCRIPTION] |
{{EXPAND: List all type theory guides}}

### Homotopy Theory

| Document | Covers |
|----------|--------|
| `topics/homotopy/GUIDE.md` | [ONE-LINE DESCRIPTION] |
| `topics/homotopy/basics.md` | [ONE-LINE DESCRIPTION] |
| `topics/homotopy/fundamental-group.md` | [ONE-LINE DESCRIPTION] |
| `topics/homotopy/higher-groups.md` | [ONE-LINE DESCRIPTION] |
| `topics/homotopy/fibrations.md` | [ONE-LINE DESCRIPTION] |
| `topics/homotopy/homology.md` | [ONE-LINE DESCRIPTION] |
{{EXPAND: List all homotopy theory guides}}

### Homotopy Type Theory

| Document | Covers |
|----------|--------|
| `topics/hott/GUIDE.md` | [ONE-LINE DESCRIPTION] |
| `topics/hott/types-as-spaces.md` | [ONE-LINE DESCRIPTION] |
| `topics/hott/univalence.md` | [ONE-LINE DESCRIPTION] |
| `topics/hott/hits.md` | [ONE-LINE DESCRIPTION] |
| `topics/hott/n-types.md` | [ONE-LINE DESCRIPTION] |
{{EXPAND: List all HoTT guides}}

### Connections

| Document | Connects |
|----------|----------|
| `connections/rosetta-stone.md` | Parallel concepts across all four fields |
| `connections/cat-type.md` | Categories as models of type theory |
| `connections/cat-homotopy.md` | ∞-categories and homotopy theory |
| `connections/groups-groupoids.md` | Groups as one-object groupoids |
| `connections/type-homotopy.md` | Identity types as path spaces |
{{EXPAND: List all connection guides}}

---

## Quick Reference

### The "Big Picture" Connections

```
                    GROUP THEORY
                         |
                         | groups are one-object
                         | groupoids
                         v
TYPE THEORY <-----> CATEGORY THEORY <-----> HOMOTOPY THEORY
      |        ^            |          ^           |
      |        |            |          |           |
      | types  | internal   | ∞-cats   | model     | spaces
      | are    | language   | as       | cats      | are
      | spaces |            | homotopy |           | ∞-groupoids
      |        |            | theories |           |
      v        |            v          |           v
      +--------+--> HOMOTOPY TYPE THEORY <---------+
                    (univalent foundations)
```

### Key Theorems to Know

| Field | Theorem | One-line summary |
|-------|---------|------------------|
| Groups | Sylow theorems | Control subgroups of prime-power order |
| Groups | Lagrange's theorem | Subgroup order divides group order |
| Categories | Yoneda lemma | Objects determined by their morphisms |
| Categories | RAPL | Right adjoints preserve limits |
| Categories | Adjoint functor theorems | When adjoints exist |
| Types | Curry-Howard | Proofs are programs, propositions are types |
| Types | Canonicity | Closed terms compute to canonical forms |
| Homotopy | Whitehead's theorem | Weak equivalences of CW complexes are homotopy equivalences |
| Homotopy | Hurewicz theorem | First nontrivial homotopy and homology agree |
| HoTT | Univalence | Equivalent types are equal |
| HoTT | Higher inductive types | Inductively define spaces by generators and paths |

### Notation Quick Reference

See `NOTATION.md` for full details. Critical conventions:

**Across all fields:**
- `→` for functions/morphisms/implications
- `≃` for equivalences (type equivalence, homotopy equivalence)
- `≅` for isomorphisms
- `≡` for definitional/judgmental equality

**Category theory:**
- `F : C → D` — functor
- `η : F ⇒ G` — natural transformation  
- `F ⊣ G` — F left adjoint to G

**Type theory:**
- `Γ ⊢ a : A` — term a has type A in context Γ
- `Π(x:A).B` — dependent product
- `Σ(x:A).B` — dependent sum
- `Id_A(x,y)` or `x =_A y` — identity type

**Homotopy:**
- `π_n(X,x₀)` — n-th homotopy group
- `[X,Y]` — homotopy classes of maps
- `~` — homotopic

---

## Maintenance Notes

### Sources

This skill synthesizes material from:

{{EXPAND: List all source documents with versions}}

### Last Updated

[DATE]

### Known Limitations

- Coverage is graduate-level; research frontiers not included
- Spectral sequences covered only briefly
- Stable homotopy theory is introductory only
- No computational algebra (GAP, Magma, etc.)

### Feedback

If Claude encounters questions these materials can't answer well, note the gap for future expansion.

---
# TEMPLATE ENDS HERE
---

## Post-Generation Checklist

After generating SKILL.md:

- [ ] **Token count:** Under 4,000 tokens
- [ ] **All files referenced exist:** Every path in Document Map is real
- [ ] **Routing is complete:** Common queries have clear routes
- [ ] **No circular references:** SKILL.md doesn't require reading itself
- [ ] **Notation matches NOTATION.md:** Symbols used consistently
- [ ] **Tested:** Sample queries route to correct documents

## Testing the SKILL.md

Run these test queries and verify routing:

1. "What is a group?" → Should route to `topics/groups/basics.md`
2. "Prove Yoneda lemma" → Should route to `topics/categories/yoneda.md`
3. "What's the connection between types and spaces?" → Should route to `connections/type-homotopy.md` or `topics/hott/`
4. "Define Π-type" → Should route to `topics/types/dependent-types.md`
5. "What is univalence?" → Should route to `topics/hott/univalence.md`
6. "How do adjunctions relate to monads?" → Should route to `topics/categories/adjunctions.md` and/or `topics/categories/monads.md`

---
```

---

## Usage Instructions

### When to Use This Prompt

Use this prompt in **Phase 5** of the workflow, after:
- ✅ All source materials have been converted
- ✅ All concept cards have been extracted  
- ✅ All topic guides have been generated
- ✅ All connection guides have been generated
- ✅ NOTATION.md and PREREQUISITES.md are finalized

### Input Required

Before running this prompt, compile:

1. **Complete file listing** of all guides with one-line descriptions
2. **Verification that all referenced files exist**
3. **The current date** for the "Last Updated" field

### Customization Points

The template has several `{{EXPAND}}` markers where you'll need to fill in project-specific details:

- Document listings for each field
- Source document versions
- Any additional connection guides

### Iteration

After initial generation:
1. Test with sample queries
2. Identify routing gaps
3. Update keyword tables and question patterns
4. Re-test

---

## Appendix: Minimal SKILL.md for Testing

If you want to test the skill infrastructure before all guides are complete, here's a minimal version:

```markdown
# Higher Mathematics Skill (DRAFT)

## Purpose
[Same as full version]

## How to Use This Skill
[Abbreviated version]

## Query Routing

| Topic | Document |
|-------|----------|
| Groups | `topics/groups/GUIDE.md` |
| Categories | `topics/categories/GUIDE.md` |
| Types | `topics/types/GUIDE.md` |
| Homotopy | `topics/homotopy/GUIDE.md` |
| HoTT | `topics/hott/GUIDE.md` |
| Notation | `NOTATION.md` |

## Status

🚧 This skill is under construction. Available guides:
- [x] `topics/categories/GUIDE.md`
- [x] `topics/categories/basics.md`
- [ ] ... (list what exists)

For topics without guides, Claude should note the gap and reason carefully from training knowledge.
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-23 | Initial prompt with embedded template |
