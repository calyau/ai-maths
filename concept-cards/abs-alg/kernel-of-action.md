---
concept: Kernel of a Group Action
slug: kernel-of-action
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
  - "kernel of an action"
prerequisites:
  - group-action
  - kernel
  - normal-subgroup
extends:
  - kernel
related:
  - stabilizer
  - faithful-action
  - permutation-representation
contrasts_with: []
answers_questions:
  - "What is the kernel of a group action?"
  - "How does the kernel of an action relate to stabilizers?"
---

# Quick Definition
The kernel of a group action of G on A is the set of elements of G that act trivially on every element of A. It equals the intersection of all point stabilizers and is a normal subgroup of G.

# Core Definition
The kernel of the action is {g in G | g . a = a for all a in A} (Dummit & Foote, p. 112). It is precisely the kernel of the associated permutation representation phi: G -> S_A. Since ker(phi) is a normal subgroup of G, the kernel of the action is normal in G. The kernel equals the intersection of all stabilizers: the intersection of G_a over all a in A.

# Prerequisites
- **Group action** — The kernel is defined relative to an action
- **Kernel** — The kernel of the action equals the kernel of the associated homomorphism
- **Normal subgroup** — The kernel is always a normal subgroup of G

# Key Properties
1. The kernel equals ker(phi), where phi is the associated permutation representation
2. The kernel is a normal subgroup of G
3. The kernel equals the intersection of all stabilizers G_a
4. The kernel is contained in every stabilizer G_a
5. Two elements g, h induce the same permutation iff they are in the same coset of the kernel

# Construction / Recognition
## To Compute the Kernel:
1. Determine which elements of G fix every element of A
2. Alternatively, compute the intersection of all point stabilizers

# Context & Application
The kernel measures how faithfully G acts on A. If the kernel is trivial, the action is faithful and G embeds in S_A. The quotient G/ker(phi) acts faithfully on A.

# Examples
**Example 1** (p. 112): S_n acting on {1,...,n} has trivial kernel.

**Example 2** (p. 113): D_8 acting on {{1,3},{2,4}} has kernel <s, r^2> of order 4.

# Relationships
## Builds Upon
- **Kernel** — Specializes the kernel concept to group actions
## Enables
- **Faithful action** — Characterized by trivial kernel
## Related
- **Stabilizer** — The kernel is the intersection of all stabilizers

# Common Errors
- **Error**: Confusing the kernel of the action with the stabilizer of a single point
  **Correction**: The kernel fixes ALL points; a stabilizer fixes one specific point

# Common Confusions
- **Confusion**: Believing the kernel can be nontrivial only for non-transitive actions
  **Clarification**: Even transitive actions can have nontrivial kernels

# Source Reference
Chapter 4: Group Actions, Section 4.1, page 112.

# Verification Notes
- Definition source: Direct from p. 112
- Confidence: HIGH — explicit definition
- Uncertainties: None
