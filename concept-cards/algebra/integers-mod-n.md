---
concept: Integers Mod n
slug: integers-mod-n
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.9 Modular Arithmetic"
extraction_confidence: high
aliases:
  - "Z/nZ"
  - "modular arithmetic"
  - "congruence classes"
prerequisites:
  - group
  - equivalence-relation
  - coset
extends: []
related:
  - quotient-group
  - prime-field
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

The set Z/nZ of integers modulo n consists of n congruence classes {0, 1, ..., n-1} with addition and multiplication defined by taking remainders after division by n. Under addition, Z/nZ is a cyclic group of order n.

# Core Definition

Two integers a and b are congruent modulo n (a ≡ b mod n) if n divides b - a. The congruence class of a is a_bar = {..., a-n, a, a+n, a+2n, ...}. There are n classes: 0, 1, ..., n-1. Sum and product are defined by a_bar + b_bar = (a+b)_bar and a_bar * b_bar = (ab)_bar (Artin, pp. 75-77). Under addition, Z/nZ is a group (in fact, a quotient group Z/Zn). When n = p is prime, Z/pZ is a field F_p.

# Prerequisites

- **Group** — Z/nZ is a group under addition
- **Equivalence relation** — Congruence modulo n is an equivalence relation
- **Coset** — Congruence classes are cosets of nZ in Z

# Key Properties

1. n congruence classes: 0, 1, ..., n-1
2. Addition and multiplication are well-defined on classes
3. Z/nZ is a cyclic group of order n under addition
4. Z/pZ is a field when p is prime (Theorem 3.2.5)
5. The map Z -> Z/nZ sending a to a_bar is a surjective homomorphism

# Construction / Recognition

## To Construct:
1. Fix a positive integer n
2. Partition Z into residue classes mod n

## To Recognize:
1. A set of n elements with addition/multiplication inherited from Z

# Context & Application

Modular arithmetic is one of the most important constructions in algebra. It provides the simplest examples of quotient groups and finite fields, and is fundamental to number theory.

# Examples

**Example 1** (p. 76): Z/29Z: (35)(17+7) can be computed as 35*24 = 6*(-5) = -30 = -1 mod 29.

**Example 2** (p. 77): There are n congruence classes modulo n (Proposition 2.9.4).

# Relationships

## Builds Upon
- **Coset** — Classes are cosets of nZ in Z

## Enables
- **Prime field** — F_p = Z/pZ when p is prime
- **Quotient group** — Z/nZ is a prototypical quotient

# Common Errors

- **Error**: Dividing congruence classes without checking invertibility
  **Correction**: Division (multiplicative inverse) exists only when the class is coprime to n

# Common Confusions

- **Confusion**: Confusing Z/nZ (congruence classes) with {0, 1, ..., n-1} (representatives)
  **Clarification**: The representatives are a convenience; the true elements are equivalence classes

# Source Reference

Chapter 2: Groups, Section 2.9, pages 75-77.

# Verification Notes

- Definition source: Direct from Section 2.9
- Confidence rationale: Extensively discussed
- Uncertainties: None
- Cross-reference status: Verified
