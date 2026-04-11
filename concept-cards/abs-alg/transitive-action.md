---
concept: Transitive Action
slug: transitive-action
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 114
section: "4.1 Group Actions and Permutation Representations"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
  - orbit
extends:
  - group-action
related:
  - orbit-stabilizer-theorem
  - cayleys-theorem
contrasts_with:
  - trivial-action
answers_questions:
  - "What does it mean for a group action to be transitive?"
  - "When does a group act transitively on a set?"
---

# Quick Definition
A group action of G on A is transitive if there is only one orbit, meaning for any two elements a, b in A there exists some g in G such that g . a = b.

# Core Definition
The action of G on A is called transitive if there is only one orbit, i.e., given any two elements a, b in A there is some g in G such that a = g . b (Dummit & Foote, p. 114). For a transitive action of a finite group, |A| = |G : G_a| for any a in A. By Theorem 3 (p. 121), the action of G by left multiplication on the cosets of any subgroup H is always transitive.

# Prerequisites
- **Group action** — Transitivity is a property of an action
- **Orbit** — Transitive means exactly one orbit

# Key Properties
1. There is exactly one orbit (which equals A)
2. |A| = |G : G_a| for any a in A
3. All stabilizers are conjugate: G_b = gG_a g^{-1} when b = g . a
4. The action of G on cosets of any subgroup H is transitive (Theorem 3)
5. The trivial action is transitive if and only if |A| = 1

# Context & Application
Transitive actions arise naturally when groups act on cosets of subgroups. Cayley's theorem uses the transitive action by left multiplication. Many classification arguments rely on transitivity of conjugation on Sylow subgroups.

# Examples
**Example 1** (p. 115): S_n acts transitively on {1,...,n}.

**Example 2** (p. 115): D_8 acts transitively on the four vertices of a square.

**Example 3** (p. 115): If G acts trivially on A, the action is transitive only if |A| = 1.

# Relationships
## Builds Upon
- **Orbit** — Transitive means a single orbit
## Enables
- **Cayleys theorem** — Uses a transitive faithful action
## Contrasts With
- **Trivial action** — Transitive only on singletons

# Common Confusions
- **Confusion**: Believing a transitive action must be faithful
  **Clarification**: Transitivity and faithfulness are independent properties. D_8 acts transitively on pairs of opposite vertices, but unfaithfully.

# Source Reference
Chapter 4: Group Actions, Section 4.1, page 114, and Theorem 3, page 121.

# Verification Notes
- Definition source: Direct from p. 114
- Confidence: HIGH — explicit definition
- Uncertainties: None
