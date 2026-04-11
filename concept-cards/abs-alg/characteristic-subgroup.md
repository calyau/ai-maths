---
concept: Characteristic Subgroup
slug: characteristic-subgroup
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 137
section: "4.4 Automorphisms"
extraction_confidence: high
aliases:
  - "characteristic in G"
prerequisites:
  - normal-subgroup
  - automorphism
extends:
  - normal-subgroup
related:
  - automorphism-group
  - inner-automorphism
contrasts_with:
  - normal-subgroup
answers_questions:
  - "What is a characteristic subgroup?"
  - "How does characteristic relate to normal?"
---

# Quick Definition
A subgroup H of G is characteristic in G (H char G) if sigma(H) = H for every automorphism sigma of G. Characteristic subgroups are automatically normal ("strongly normal"). A characteristic subgroup of a normal subgroup is normal in the whole group.

# Core Definition
A subgroup H of a group G is called characteristic in G, denoted H char G, if every automorphism of G maps H to itself, i.e., sigma(H) = H for all sigma in Aut(G) (Dummit & Foote, p. 137). Key properties: (1) characteristic subgroups are normal; (2) if H is the unique subgroup of G of a given order, then H is characteristic; (3) if K char H and H is normal in G, then K is normal in G.

# Prerequisites
- **Normal subgroup** — Characteristic implies normal
- **Automorphism** — Characteristic means invariant under ALL automorphisms

# Key Properties
1. Characteristic implies normal (since inner automorphisms are automorphisms)
2. Unique subgroup of a given order is characteristic
3. K char H and H normal in G implies K normal in G (transitivity for char + normal)
4. K char H and H char G implies K char G
5. Normal subgroups of a normal subgroup need not be normal, but characteristic subgroups of normal subgroups are

# Examples
**Example 1** (p. 137): Every subgroup of a cyclic group is characteristic.

**Example 2**: The center Z(G) is always characteristic. The commutator subgroup G' is characteristic.

**Example 3**: A normal subgroup that is NOT characteristic: V_4 = {e, (12)(34), (13)(24), (14)(23)} is normal in A_4, and <(12)(34)> is normal in V_4 but not normal in A_4.

# Relationships
## Builds Upon
- **Normal subgroup** — Characteristic is a stronger condition
## Enables
- **Transitivity results** — Char of normal is normal
## Contrasts With
- **Normal subgroup** — Normal means invariant under inner automorphisms only; characteristic means invariant under ALL automorphisms

# Source Reference
Chapter 4, Section 4.4, page 137.

# Verification Notes
- Definition source: Direct from p. 137
- Confidence: HIGH
- Uncertainties: None
