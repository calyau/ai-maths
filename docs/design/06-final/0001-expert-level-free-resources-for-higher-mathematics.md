---
number: 1
title: "Expert-Level Free Resources for Higher Mathematics"
author: "Duncan McGreggor"
component: All
tags: [change-me]
created: 2026-01-24
updated: 2026-01-24
state: Final
supersedes: null
superseded-by: null
version: 1.0
---

# Expert-Level Free Resources for Higher Mathematics

## Overview

This document compiles high-quality, freely available resources for four interconnected areas of modern mathematics: **Group Theory**, **Type Theory**, **Category Theory**, and **Homotopy Theory**. These areas increasingly converge in contemporary research, particularly through Homotopy Type Theory (HoTT).

---

## 1. GROUP THEORY

### Primary Textbooks (Free)

| Resource | Author(s) | Level | URL |
|----------|-----------|-------|-----|
| **Group Theory** | J.S. Milne | Graduate | https://www.jmilne.org/math/CourseNotes/GT.pdf |
| **Abstract Algebra: Theory and Applications** | Tom Judson | Undergrad/Graduate | http://abstract.ups.edu/ |
| **Introduction to Lie Groups and Lie Algebras** | Alexander Kirillov Jr. | Graduate | SUNY Stony Brook (free online) |
| **Algebraic Groups, Lie Groups, and their Arithmetic Subgroups** | J.S. Milne | Advanced Graduate | https://www.jmilne.org/math/ |

### Lecture Notes & Supplementary

- **Combinatorial Group Theory** — Charles F. Miller III (University of Melbourne)
- **Introduction to Groups, Invariants and Particles** — Frank W.K. Firk
- **Elements of Group Theory** — Ferdi Aryasetiawan (University of Lund)

### Topics Covered
- Basic group axioms, subgroups, quotients
- Sylow theorems, solvable and nilpotent groups
- Group actions and representations
- Lie groups and Lie algebras
- Representation theory

---

## 2. TYPE THEORY

### Foundational Texts (Free)

| Resource | Author(s) | Level | URL |
|----------|-----------|-------|-----|
| **Intuitionistic Type Theory (1984 Bibliopolis)** | Per Martin-Löf | Graduate | https://archive-pml.github.io/martin-lof/pdfs/Bibliopolis-Book-retypeset-1984.pdf |
| **Programming in Martin-Löf's Type Theory** | Nordström, Petersson, Smith | Graduate | https://www.cse.chalmers.se/research/group/logic/book/book.pdf |
| **Programming Language Foundations in Agda (PLFA)** | Wadler, Kokke, Siek | Graduate | https://plfa.github.io/ |
| **Stanford Encyclopedia: Intuitionistic Type Theory** | — | Survey | https://plato.stanford.edu/entries/type-theory-intuitionistic/ |

### Key References

- **Martin-Löf's Type Theory** — Nordström, Petersson, Smith (Handbook chapter): https://www.cse.chalmers.se/~smith/handbook.pdf
- **Syntax and Semantics of Dependent Types** — Martin Hofmann
- **nLab article on Martin-Löf dependent type theory**: https://ncatlab.org/nlab/show/Martin-L%C3%B6f+dependent+type+theory

### Core Concepts
- Dependent types (Π-types, Σ-types)
- Identity types
- Judgments and contexts
- Propositions-as-types (Curry-Howard correspondence)
- Universes and type hierarchies
- Intensional vs. extensional type theory

---

## 3. CATEGORY THEORY

### Primary Textbooks (Free)

| Resource | Author(s) | Level | URL |
|----------|-----------|-------|-----|
| **Category Theory in Context** | Emily Riehl | Undergrad/Graduate | https://emilyriehl.github.io/files/context.pdf |
| **Basic Category Theory** | Tom Leinster | Introductory | https://arxiv.org/abs/1612.09375 |
| **Category Theory** (lecture notes) | Steve Awodey | Graduate | Available via Carnegie Mellon |
| **Categories for the Working Mathematician** | Saunders Mac Lane | Graduate | (classic reference, check library) |

### Additional Free Resources

- **nLab** — Comprehensive wiki for category theory and higher structures: https://ncatlab.org/
- **Categorical Homotopy Theory** — Emily Riehl (free PDF): https://emilyriehl.github.io/
- **Seven Sketches in Compositionality** — Fong & Spivak (applied category theory)
- **Category Theory for Scientists** — David Spivak (arXiv)

### Curated Resource List
- **Logic Matters** category theory page: https://www.logicmatters.net/categories/

### Core Concepts
- Categories, functors, natural transformations
- Universal properties, representability
- Yoneda lemma
- Limits and colimits
- Adjunctions
- Monads
- Kan extensions

---

## 4. HOMOTOPY THEORY (including Homotopy Type Theory)

### Classical Algebraic Topology / Homotopy Theory

| Resource | Author(s) | Level | URL |
|----------|-----------|-------|-----|
| **Algebraic Topology** | Allen Hatcher | Graduate | https://pi.math.cornell.edu/~hatcher/AT/AT.pdf |
| **A Concise Course in Algebraic Topology** | J.P. May | Graduate | University of Chicago Press |
| **Homotopy Theory for Beginners** | Jesper M. Møller | Introductory | https://ncatlab.org/nlab/files/Moller_HomotopyTheory.pdf |

### Homotopy Type Theory (HoTT)

| Resource | Author(s) | Level | URL |
|----------|-----------|-------|-----|
| **Homotopy Type Theory: Univalent Foundations of Mathematics** (The HoTT Book) | Univalent Foundations Program | Graduate | https://homotopytypetheory.org/book/ |
| **Introduction to Homotopy Type Theory** | Egbert Rijke | Graduate | https://ncatlab.org/nlab/files/Rijke-IntroductionHoTT-2018.pdf |
| **Introduction to HoTT** (slides) | Emily Riehl | Survey | https://emilyriehl.github.io/files/Intro-HoTT-UF.pdf |
| **A Primer on Homotopy Type Theory** | — | Introductory | https://philsci-archive.pitt.edu/11157/1/HTT_Primer-PART-1.pdf |

### nLab Resources (Authoritative Wiki)

- **Homotopy Theory**: https://ncatlab.org/nlab/show/homotopy+theory
- **Introduction to Homotopy Theory**: https://ncatlab.org/nlab/show/Introduction+to+Homotopy+Theory
- **Introduction to Stable Homotopy Theory**: https://ncatlab.org/nlab/show/Introduction+to+Stable+Homotopy+Theory
- **Homotopy Type Theory**: https://ncatlab.org/nlab/show/homotopy+type+theory
- **References page**: https://ncatlab.org/nlab/show/homotopy+theory+and+algebraic+topology+--+references

### Core Concepts (Classical)
- Homotopy and homotopy equivalence
- Fundamental group and higher homotopy groups
- CW complexes
- Fibrations and cofibrations
- Homology and cohomology
- Spectral sequences
- Model categories

### Core Concepts (HoTT)
- Univalence axiom
- Higher inductive types
- n-types and truncation levels
- Path spaces as identity types
- Synthetic homotopy theory

---

## 5. INTERCONNECTIONS & LEARNING PATHS

### The Convergence Point: Homotopy Type Theory

HoTT sits at the intersection of all four areas:
- **Type Theory** provides the formal system
- **Category Theory** provides the semantic models (∞-toposes)
- **Homotopy Theory** provides the intuition and applications
- **Group Theory** appears via π₁, automorphism groups, and ∞-groupoids

### Suggested Learning Paths

**Path A: Algebraic/Geometric Focus**
1. Group Theory (Milne or Judson)
2. Category Theory (Riehl or Leinster)
3. Algebraic Topology (Hatcher)
4. HoTT Book

**Path B: Type-Theoretic/Foundational Focus**
1. Category Theory (Awodey or Riehl)
2. Type Theory (Martin-Löf / Nordström-Petersson-Smith)
3. PLFA (practical type theory in Agda)
4. HoTT Book

**Path C: For Programmers/Computer Scientists**
1. PLFA
2. Category Theory (Awodey, with CS flavor)
3. HoTT Book
4. Backfill homotopy theory as needed

---

## 6. ESSENTIAL ONLINE REFERENCES

### Wikis & Living Documents
- **nLab**: https://ncatlab.org/ — The definitive wiki for higher category theory, homotopy theory, and mathematical physics
- **Stacks Project**: https://stacks.math.columbia.edu/ — For algebraic geometry connections

### Blogs & Discussion
- **n-Category Café**: https://golem.ph.utexas.edu/category/ — Research blog
- **Homotopy Type Theory site**: https://homotopytypetheory.org/
- **MathOverflow**: For research-level questions

### Proof Assistants (for computational exploration)
- **Agda**: Dependently-typed programming language
- **Coq/Rocq**: Proof assistant with tactics
- **Lean**: Modern proof assistant with mathlib

---

## 7. BIBLIOGRAPHY FORMAT

For each resource, when building the SKILL.md, include:

```
### [Resource Name]
- **Author(s)**: 
- **Type**: Textbook / Lecture Notes / Wiki
- **Level**: Introductory / Graduate / Research
- **URL**: 
- **Topics**: 
- **Prerequisites**: 
- **Recommended Sections for [specific topic]**: 
```

---

## Notes for SKILL.md Development

1. **nLab should be the primary reference** for definitions and theorems — it's comprehensive, peer-edited, and reflects current understanding

2. **Cross-reference extensively** — these subjects are deeply interconnected; a concept in one area often illuminates another

3. **Include worked examples** — abstract definitions need concrete instantiations

4. **Proof verification** — for HoTT specifically, proofs can be machine-checked in Agda or Coq

5. **Version control** — mathematics evolves; note when resources were last updated

6. **Notation conventions** — different authors use different conventions; document them explicitly
