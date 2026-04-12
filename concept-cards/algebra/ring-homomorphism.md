---
concept: Ring Homomorphism
slug: ring-homomorphism
category: ring-theory
subcategory: morphisms
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Homomorphisms and Ideals"
extraction_confidence: high
aliases:
  - "homomorphism of rings"
prerequisites:
  - ring
extends: []
related:
  - ring-isomorphism
  - kernel-of-ring-homomorphism
  - substitution-principle
contrasts_with: []
answers_questions:
  - "What is a ring homomorphism?"
---

# Quick Definition

A ring homomorphism is a map between rings that preserves addition, multiplication, and sends 1 to 1.

# Core Definition

A ring homomorphism phi: R -> R' is a map from one ring to another which satisfies, for all a and b in R: phi(a+b) = phi(a) + phi(b), phi(ab) = phi(a)phi(b), and phi(1) = 1 (Artin, Section 11.3, formula 11.3.1, p. 344).

# Prerequisites

- **Ring** -- Homomorphisms are maps between rings

# Key Properties

1. Preserves addition (is a group homomorphism on additive groups)
2. Preserves multiplication
3. Sends 1 to 1 (must be stated separately; does not follow from multiplication)
4. phi(0) = 0 (follows from additive group homomorphism)
5. The zero map is NOT a ring homomorphism unless the target is the zero ring

# Construction / Recognition

## To Recognize:
1. Verify phi(a+b) = phi(a) + phi(b) for all a, b
2. Verify phi(ab) = phi(a)phi(b) for all a, b
3. Verify phi(1) = 1

# Context & Application

The most important ring homomorphisms come from evaluating polynomials. The substitution map that sends f(x) to f(alpha) is a ring homomorphism whose kernel yields key algebraic information.

# Examples

**Example 1** (p. 344): The map Z -> F_p sending an integer to its congruence class modulo p is a ring homomorphism.

**Example 2** (p. 344): Evaluation of real polynomials at a real number a defines a homomorphism R[x] -> R.

# Relationships

## Builds Upon
- **Ring** -- Source and target are rings

## Enables
- **Kernel of ring homomorphism** -- The kernel is an ideal
- **First Isomorphism Theorem** -- Relates quotient rings to images of homomorphisms

# Common Errors

- **Error**: Assuming compatibility with multiplication implies phi(1) = 1
  **Correction**: The condition phi(1) = 1 must be checked separately since R is not a group under multiplication

# Source Reference

Chapter 11: Rings, Section 11.3, pages 344-345.

# Verification Notes

- Definition source: Direct from formula 11.3.1
- Confidence rationale: Explicit definition with all three conditions
- Uncertainties: None
- Cross-reference status: Verified
