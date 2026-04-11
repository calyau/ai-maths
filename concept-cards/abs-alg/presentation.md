---
concept: Presentation of a Group
slug: presentation
category: group-theory
subcategory: further-topics
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Further Topics in Group Theory"
chapter_number: 6
pdf_page: 221
section: "6.3 A Word on Free Groups"
extraction_confidence: high
aliases:
  - "group presentation"
  - "generators and relations"
prerequisites:
  - free-group
  - normal-subgroup
  - quotient-group
  - homomorphism
extends:
  - free-group
related:
  - generators-and-relations
contrasts_with: []
answers_questions:
  - "What is a presentation of a group?"
  - "How do generators and relations define a group?"
---

# Quick Definition
A presentation of a group G is a pair (S, R) where S is a generating set and R is a set of words in the free group F(S) whose normal closure equals the kernel of the natural surjection F(S) -> G. We write G = <s_1, ..., s_n | w_1 = ... = w_k = 1>.

# Core Definition
Let S be a subset of G such that G = <S>. A presentation for G is a pair (S, R), where R is a set of words in F(S) such that the normal closure of <R> in F(S) equals the kernel of the homomorphism pi: F(S) -> G extending the identity on S (Dummit & Foote, p. 221). Elements of S are generators and elements of R are relations. G is finitely presented if both S and R are finite.

# Prerequisites
- **Free group** — Presentations use quotients of free groups
- **Normal subgroup** — Relations generate a normal subgroup
- **Quotient group** — G = F(S) / (normal closure of R)
- **Homomorphism** — The presentation homomorphism pi: F(S) -> G

# Key Properties
1. G is isomorphic to F(S) / (normal closure of R)
2. Every finite group is finitely presented
3. Different presentations can define the same group
4. If a', b' in a group H satisfy the relations in R, there is a homomorphism G -> H
5. It is in general undecidable whether a given presentation defines the trivial group

# Examples
**Example 1** (p. 222): D_{2n} = <r, s | r^n = s^2 = 1, s^{-1}rs = r^{-1}>.

**Example 2** (p. 222): Q_8 = <i, j | i^4 = 1, j^2 = i^2, j^{-1}ij = i^{-1}>.

**Example 3** (p. 223): S_n = <t_1, ..., t_{n-1} | t_i^2 = 1, (t_i t_{i+1})^3 = 1, [t_i, t_j] = 1 for |i-j| >= 2>.

**Example 4** (p. 223): The presentation <x_1, x_2, x_3 | x_2 x_1 x_2^{-1} = x_1^2, x_3 x_2 x_3^{-1} = x_2^2, x_1 x_3 x_1^{-1} = x_3^2> defines the trivial group.

# Relationships
## Builds Upon
- **Free group** — G = F(S) modulo relations
## Enables
- **Constructing homomorphisms** — Maps respecting relations give homomorphisms
- **Determining automorphisms** — Automorphisms must map generators to generators satisfying the same relations

# Common Confusions
- **Confusion**: Thinking a presentation uniquely determines a "nice" group
  **Clarification**: It can be extremely difficult or impossible to determine basic properties (like the order) from a presentation

# Source Reference
Chapter 6, Section 6.3, pages 221-224.

# Verification Notes
- Definition source: Direct from p. 221
- Confidence: HIGH
- Uncertainties: None
