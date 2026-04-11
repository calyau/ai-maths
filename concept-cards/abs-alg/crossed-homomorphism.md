---
concept: Crossed Homomorphism
slug: crossed-homomorphism
category: homological-algebra
subcategory: group-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 810
section: "17.3 Crossed Homomorphisms and H^1(G,A)"
extraction_confidence: high
aliases:
  - "1-cocycle"
  - "principal crossed homomorphism"
  - "1-coboundary"
prerequisites:
  - group-cohomology
extends: []
related:
  - group-extension
contrasts_with: []
answers_questions:
  - "What is a crossed homomorphism?"
  - "What does H^1(G,A) classify?"
---

# Quick Definition
A crossed homomorphism f: G → A satisfies f(gh) = gf(h) + f(g). Those of the form f(g) = ga - a are principal. H^1(G,A) = crossed hom. / principal crossed hom.

# Core Definition
A function f: G → A is a **crossed homomorphism** (or 1-cocycle) if f(gh) = gf(h) + f(g) for all g,h ∈ G (Definition, p. 810). A **principal crossed homomorphism** (or 1-coboundary) has the form f(g) = ga - a for some fixed a ∈ A. Then H^1(G,A) = {crossed homomorphisms} / {principal crossed homomorphisms}.

# Prerequisites
- **group-cohomology** — H^1 is the first cohomology group

# Key Properties
1. When G acts trivially, crossed homomorphisms are just group homomorphisms
2. H^1(G,A) = Hom(G,A) when G acts trivially on A
3. H^1(G,A) appears in the long exact sequence from 0 → A → B → C → 0

# Relationships
## Builds Upon
- **group-cohomology** — H^1 is defined via crossed homomorphisms

# Source Reference
Chapter 17, Section 17.3, Definition and characterizations, pages 810-820.

# Verification Notes
- Confidence: HIGH — explicit definition and identification with H^1
