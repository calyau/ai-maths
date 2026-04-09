---
# === CORE IDENTIFICATION ===
concept: Unique Factorization Domain
slug: unique-factorization-domain

# === CLASSIFICATION ===
category: domain-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Integral Domains"
chapter_number: 18
pdf_page: 243
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "UFD"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integral-domain
  - irreducible-element
  - associates-in-integral-domains
extends:
  - integral-domain
related:
  - principal-ideal-domain
  - euclidean-domain
contrasts_with:
  - principal-ideal-domain

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a unique factorization domain?"
  - "What distinguishes a PID from a UFD?"
  - "How do rings relate to integral domains and fields?"
---

# Quick Definition

A unique factorization domain (UFD) is an integral domain in which every nonzero, non-unit element can be written as a product of irreducibles, and this factorization is unique up to order and associates.

# Core Definition

An integral domain $D$ is a unique factorization domain if: (1) every nonzero non-unit $a \in D$ can be written as a product of irreducible elements; and (2) if $a = p_1 \cdots p_r = q_1 \cdots q_s$ with all $p_i, q_j$ irreducible, then $r = s$ and there is a permutation such that $p_i$ and $q_{\pi(i)}$ are associates (Judson, p. 243).

# Prerequisites

- **Integral domain** — A UFD is an integral domain
- **Irreducible element** — Factorizations are into irreducibles
- **Associates** — Uniqueness is up to associates

# Key Properties

1. Existence: every nonzero non-unit factors into irreducibles
2. Uniqueness: factorization unique up to order and associates
3. Every PID is a UFD (Theorem 18.15)
4. $D$ is a UFD $\Rightarrow$ $D[x]$ is a UFD (Theorem 18.29)
5. $\mathbb{Z}[x]$ is a UFD but not a PID (Example 18.17)

# Construction / Recognition

## To Verify:
1. Confirm $D$ is an integral domain
2. Show every nonzero non-unit factors into irreducibles
3. Show the factorization is unique up to order and associates

# Context & Application

UFDs generalize the Fundamental Theorem of Arithmetic to arbitrary domains. The hierarchy is: Euclidean domain $\subset$ PID $\subset$ UFD $\subset$ integral domain. Not all integral domains are UFDs (e.g., $\mathbb{Z}[\sqrt{3}i]$).

# Examples

**Example 1** (p. 243): $\mathbb{Z}$ is a UFD by the Fundamental Theorem of Arithmetic.

**Example 2** (p. 243): $\mathbb{Z}[\sqrt{3}i]$ is NOT a UFD: $4 = 2 \cdot 2 = (1 - \sqrt{3}i)(1 + \sqrt{3}i)$ gives two distinct factorizations into irreducibles.

**Example 3** (p. 245): $\mathbb{Z}[x]$ is a UFD (Corollary 18.31) but not a PID (Example 18.17).

# Relationships

## Builds Upon
- **Integral domain** — A UFD is an integral domain with unique factorization

## Enables
- **$D[x]$ is a UFD** — If $D$ is a UFD, so is $D[x]$

## Contrasts With
- **PID** — Every PID is a UFD, but $\mathbb{Z}[x]$ is a UFD that is not a PID

# Common Errors

- **Error**: Assuming every integral domain is a UFD
  **Correction**: $\mathbb{Z}[\sqrt{3}i]$ is an integral domain but not a UFD

# Common Confusions

- **Confusion**: Thinking UFD means "every element has a unique factorization"
  **Clarification**: Units and zero are excluded; factorizations are unique only up to order and associates

# Source Reference

Chapter 18: Integral Domains, Section 18.2, pages 243-245. See Theorem 18.15 and Examples 18.9, 18.10.

# Verification Notes

- Definition source: Direct from p. 243
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
