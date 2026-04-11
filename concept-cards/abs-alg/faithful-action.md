---
concept: Faithful Action
slug: faithful-action
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
  - "effective action"
prerequisites:
  - group-action
  - kernel
extends:
  - group-action
related:
  - permutation-representation
  - cayleys-theorem
contrasts_with:
  - trivial-action
answers_questions:
  - "What does it mean for a group action to be faithful?"
  - "When does a group embed into a symmetric group via an action?"
---

# Quick Definition
An action of a group G on a set A is faithful if its kernel is the identity, meaning the only element of G that fixes every element of A is the identity element. Equivalently, the associated permutation representation is injective.

# Core Definition
An action is faithful if its kernel is the identity: {g in G | g . a = a for all a in A} = {1} (Dummit & Foote, p. 112). This means the associated permutation representation phi: G -> S_A is injective, so G is isomorphic to a subgroup of S_A.

# Prerequisites
- **Group action** — Faithfulness is a property of a group action
- **Kernel** — The kernel of the action must be trivial for faithfulness

# Key Properties
1. The kernel of a faithful action is {1}
2. The associated permutation representation is injective
3. G is isomorphic to a subgroup of S_A via a faithful action
4. Two group elements induce the same permutation if and only if they differ by an element of the kernel; for faithful actions, distinct elements induce distinct permutations

# Construction / Recognition
## To Verify Faithfulness:
1. Compute the kernel of the action: all g in G with g . a = a for all a in A
2. Check that this kernel is trivial (equals {1})

## To Construct a Faithful Action:
1. Find a homomorphism phi: G -> S_A that is injective
2. Define the action by g . a = phi(g)(a)

# Context & Application
Faithful actions are important because they allow groups to be studied concretely as permutation groups. Cayley's Theorem shows every group has a faithful action (on itself by left multiplication). Faithful actions are central to proving that abstract groups can be realized as subgroups of symmetric groups.

# Examples
**Example 1** (p. 112): S_n acts faithfully on {1, 2, ..., n} since only the identity permutation fixes all elements.

**Example 2** (p. 112): D_8 acts faithfully on the four vertices of a square since only the identity symmetry fixes all four vertices.

**Example 3** (p. 113): D_8 acting on {{1,3}, {2,4}} is NOT faithful: its kernel is <s, r^2>, a subgroup of order 4.

# Relationships
## Builds Upon
- **Group action** — Faithfulness is a property of an action

## Enables
- **Cayleys theorem** — Uses a faithful action to embed G into S_n

## Related
- **Permutation representation** — A faithful action gives an injective permutation representation

## Contrasts With
- **Trivial action** — Every element acts as identity; maximally unfaithful

# Common Errors
- **Error**: Assuming every group action is faithful
  **Correction**: Many natural actions have nontrivial kernel (e.g., D_8 on pairs of opposite vertices)

# Common Confusions
- **Confusion**: Confusing faithful action with free action
  **Clarification**: Faithful means no element (except identity) fixes ALL points; free means no element (except identity) fixes ANY point. Free implies faithful but not conversely.

# Source Reference
Chapter 4: Group Actions, Section 4.1, page 112. Definition and Examples 1-4.

# Verification Notes
- Definition source: Direct from p. 112
- Confidence: HIGH — explicit definition
- Uncertainties: None
