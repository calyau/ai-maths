---
concept: Group Action
slug: group-action
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 112
section: "4.1 Group Actions and Permutation Representations"
extraction_confidence: high
aliases:
  - "G-set"
  - "G-action"
  - "left group action"
prerequisites:
  - group
  - homomorphism
  - symmetric-group
extends:
  - group
related:
  - permutation-representation
  - orbit
  - stabilizer
  - faithful-action
contrasts_with:
  - right-group-action
answers_questions:
  - "What does it mean for a group to act on a set?"
  - "How are group actions related to homomorphisms into symmetric groups?"
  - "What distinguishes a group from a monoid via group actions?"
---

# Quick Definition
A group action of a group G on a nonempty set A is a map from G x A to A satisfying two axioms: (1) g1 . (g2 . a) = (g1 g2) . a, and (2) 1 . a = a for all g1, g2 in G and a in A. The invertibility of group elements (distinguishing groups from monoids) ensures each element acts as a bijection on A.

# Core Definition
Let G be a group acting on a nonempty set A. For each g in G, the map sigma_g: A -> A defined by sigma_g(a) = g . a is a permutation of A. There is an associated homomorphism phi: G -> S_A defined by phi(g) = sigma_g, called the permutation representation associated to the given action (Dummit & Foote, p. 112). By Proposition 1, there is a bijection between the actions of G on A and the homomorphisms of G into S_A.

# Prerequisites
- **Group** — The acting object must satisfy the group axioms; invertibility of elements ensures each acts as a bijection
- **Homomorphism** — Actions correspond bijectively to homomorphisms into symmetric groups
- **Symmetric group** — The codomain of the associated permutation representation

# Key Properties
1. Each group element acts as a permutation (bijection) of the set A
2. The identity element acts as the identity permutation
3. The action is compatible with group multiplication: g1 . (g2 . a) = (g1 g2) . a
4. There is a bijection between actions of G on A and homomorphisms G -> S_A (Proposition 1)
5. The kernel of the action equals the kernel of the associated permutation representation
6. The kernel is a normal subgroup of G

# Construction / Recognition
## To Construct a Group Action:
1. Define a map G x A -> A, denoted g . a
2. Verify axiom 1: g1 . (g2 . a) = (g1 g2) . a for all g1, g2 in G and a in A
3. Verify axiom 2: 1 . a = a for all a in A

## To Recognize a Group Action:
1. Identify the group G and the set A
2. Check that each group element defines a permutation of A
3. Verify the two axioms hold

# Context & Application
Group actions are one of the fundamental unifying themes in Dummit & Foote. The concept recurs in the study of modules, vector spaces, canonical forms for matrices, and Galois Theory. When more structure is added to the set on which the group acts, more information about the group becomes available. The study of group actions culminates in the proof of Sylow's Theorem.

# Examples
**Example 1** (p. 112): S_n acts on {1, 2, ..., n} by sigma . i = sigma(i). The permutation representation is the identity map S_n -> S_n. This action is faithful.

**Example 2** (p. 112): D_8 acts on the four vertices of a square. With r = rotation by pi/2 and s = reflection through vertices 1 and 3, sigma_r = (1 2 3 4) and sigma_s = (2 4). This action is faithful; the stabilizer of any vertex has order 2.

**Example 3** (p. 113): D_8 acts on the set of unordered pairs of opposite vertices {{1,3}, {2,4}}. This action is not faithful: its kernel is <s, r^2>.

# Relationships
## Builds Upon
- **Group** — A group action requires a group as the acting object
- **Symmetric group** — Actions correspond to homomorphisms into symmetric groups

## Enables
- **Orbit** — Orbits partition the set under the action
- **Stabilizer** — Stabilizers are subgroups arising from the action
- **Permutation representation** — Every action affords a permutation representation
- **Cayleys theorem** — Follows from the action of G on itself by left multiplication
- **Class equation** — Follows from the conjugation action
- **Sylow theorems** — Proved using specific group actions

## Related
- **Faithful action** — Special case where the kernel is trivial
- **Transitive action** — Special case with a single orbit

## Contrasts With
- **Right group action** — Uses the convention a . g instead of g . a, with axiom (a . g1) . g2 = a . (g1 g2)

# Common Errors
- **Error**: Forgetting to verify both axioms when defining an action
  **Correction**: Both the compatibility axiom and the identity axiom must be checked

- **Error**: Assuming D_8 acts on any set of pairs of vertices
  **Correction**: D_8 does not act on {{1,2},{3,4}} because r . {1,2} = {2,3} is not in the set (Example 4, p. 113)

# Common Confusions
- **Confusion**: Believing the kernel of an action is the same as the stabilizer of a point
  **Clarification**: The kernel is the intersection of all stabilizers; it consists of elements fixing every point, while a stabilizer fixes only one specific point

- **Confusion**: Thinking a group action requires the group to be a subgroup of S_A
  **Clarification**: Any homomorphism phi: G -> S_A defines an action; G need not embed in S_A (the homomorphism may have nontrivial kernel)

# Source Reference
Chapter 4: Group Actions, Section 4.1 "Group Actions and Permutation Representations," pages 112-120. See especially Proposition 1 (bijection between actions and homomorphisms) and Examples 1-4.

# Verification Notes
- Definition source: Direct from p. 112, combining the definition with Proposition 1
- Key Properties: Items 1-6 explicit in source
- Examples: Directly from source Examples 1-4 on pp. 112-113
- Confidence: HIGH — explicit definition with extensive examples
- Cross-references: All slug references correspond to planned extractions
- Uncertainties: None
