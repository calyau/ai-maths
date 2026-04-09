---
# === CORE IDENTIFICATION ===
concept: Euclidean Domain
slug: euclidean-domain

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
pdf_page: 245
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integral-domain
  - euclidean-valuation
extends:
  - integral-domain
related:
  - principal-ideal-domain
  - gaussian-integers
contrasts_with:
  - principal-ideal-domain

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Euclidean domain?"
  - "How do Euclidean domains relate to PIDs?"
---

# Quick Definition

A Euclidean domain is an integral domain $D$ equipped with a function $\nu : D \setminus \{0\} \to \mathbb{N}$ (a Euclidean valuation) that enables a division algorithm: for any $a, b \in D$ with $b \neq 0$, there exist $q, r$ with $a = bq + r$ and either $r = 0$ or $\nu(r) < \nu(b)$.

# Core Definition

An integral domain $D$ with a function $\nu : D \setminus \{0\} \to \mathbb{N}$ is a Euclidean domain if: (1) $\nu(a) \leq \nu(ab)$ for all nonzero $a, b$; (2) for all $a, b \in D$ with $b \neq 0$, there exist $q, r \in D$ with $a = bq + r$ and either $r = 0$ or $\nu(r) < \nu(b)$ (Judson, pp. 245-246).

# Prerequisites

- **Integral domain** — A Euclidean domain is an integral domain
- **Euclidean valuation** — The valuation function $\nu$ enables division

# Key Properties

1. Has a division algorithm
2. Every Euclidean domain is a PID (Theorem 18.21)
3. Every Euclidean domain is a UFD (Corollary 18.22)
4. The Euclidean algorithm computes GCDs
5. Hierarchy: Euclidean domain $\subset$ PID $\subset$ UFD

# Construction / Recognition

## To Verify:
1. Confirm $D$ is an integral domain
2. Find a function $\nu : D \setminus \{0\} \to \mathbb{N}$
3. Verify $\nu(a) \leq \nu(ab)$
4. Verify the division property

# Context & Application

Euclidean domains are the most computationally tractable integral domains because they support a division algorithm and hence the Euclidean algorithm for GCDs.

# Examples

**Example 1** (p. 246): $\mathbb{Z}$ with $\nu(a) = |a|$ is a Euclidean domain.

**Example 2** (p. 246): $F[x]$ with $\nu(p(x)) = \deg p(x)$ for any field $F$.

**Example 3** (p. 246): The Gaussian integers $\mathbb{Z}[i]$ with $\nu(a + bi) = a^2 + b^2$.

# Relationships

## Builds Upon
- **Integral domain** — A Euclidean domain is an integral domain

## Enables
- **PID** — Every Euclidean domain is a PID (Theorem 18.21)
- **UFD** — Every Euclidean domain is a UFD (Corollary 18.22)

## Contrasts With
- **PID** — There exist PIDs that are not Euclidean domains

# Common Errors

- **Error**: Assuming every PID is a Euclidean domain
  **Correction**: There exist PIDs that are not Euclidean domains (though examples are subtle)

# Common Confusions

- **Confusion**: Thinking the Euclidean valuation is unique
  **Clarification**: Multiple valuations can make the same domain Euclidean

# Source Reference

Chapter 18: Integral Domains, Section 18.2, pages 245-247. See Theorem 18.21 and Examples 18.18-18.20.

# Verification Notes

- Definition source: Direct from pp. 245-246
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
