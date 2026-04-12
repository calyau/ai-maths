---
concept: "Cayley's Theorem"
slug: cayleys-theorem
category: group-theory
subcategory: structure-theorems
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.1 Cayley's Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
  - faithful-action
  - permutation-representation
extends: []
related:
  - conjugacy-class
contrasts_with: []
answers_questions:
  - "What is Cayley's theorem?"
---

# Quick Definition

Cayley's Theorem states that every finite group is isomorphic to a subgroup of a permutation group. A group of order n embeds into S_n via the faithful action of left multiplication on itself.

# Core Definition

Every finite group is isomorphic to a subgroup of a permutation group. A group of order n is isomorphic to a subgroup of the symmetric group S_n (Artin, Theorem 7.1.3, p. 206). The proof uses left multiplication: G acts on itself by g*x = gx. This action is transitive and faithful (stabilizer of any element is trivial), so the permutation representation G -> Perm(G) = S_n is injective.

# Prerequisites

- **Group action** — Uses the left multiplication action
- **Faithful action** — Left multiplication is faithful
- **Permutation representation** — The injective homomorphism G -> S_n

# Key Properties

1. Every finite group embeds in some S_n
2. The embedding uses left multiplication
3. The action is transitive with trivial stabilizers
4. Difficult to use in practice because |S_n| = n! is usually much larger than n

# Construction / Recognition

## To Apply:
1. Let G act on itself by left multiplication
2. Each g in G determines a permutation of the n elements of G
3. This gives an injective homomorphism G -> S_n

# Context & Application

Cayley's Theorem is theoretically important but practically limited because S_n is too large. More useful are the specific permutation representations from actions on cosets (which give embeddings into smaller symmetric groups).

# Examples

**Example 1** (p. 206): Left multiplication by g maps x to gx for all x in G. The stabilizer of any element is {1}, so the action is faithful.

# Relationships

## Builds Upon
- **Faithful action** — Left multiplication is faithful
- **Permutation representation** — Gives the embedding

## Related
- **Conjugation** — A more subtle and useful action than left multiplication

# Common Confusions

- **Confusion**: Thinking Cayley's Theorem gives the most efficient embedding
  **Clarification**: The embedding into S_n is usually far from optimal; actions on cosets give smaller representations

# Source Reference

Chapter 7: More Group Theory, Section 7.1, Theorem 7.1.3, p. 206.

# Verification Notes

- Definition source: Direct from Theorem 7.1.3
- Confidence rationale: Named theorem, explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
