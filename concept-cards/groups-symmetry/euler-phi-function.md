---
# === CORE IDENTIFICATION ===
concept: Euler's Phi-Function
slug: euler-phi-function

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Lagrange's Theorem"
chapter_number: 11
pdf_page: 64
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Euler's totient function"
  - "$\\varphi(n)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - r-n-group
extends: []
related:
  - euler-theorem
  - fermat-little-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Euler's phi-function?"
  - "How many integers less than n are coprime to n?"
---

# Quick Definition

Euler's phi-function $\varphi(n)$ counts the number of integers between 1 and $n-1$ that are coprime to $n$. Equivalently, it is the order of the group $R_n$.

# Core Definition

The order of $R_n$ is written $\varphi(n)$ and $\varphi$ is called Euler's phi-function (Armstrong, Ch. 11, p. 65).

# Prerequisites

- **Group of units modulo $n$** — $\varphi(n) = |R_n|$

# Key Properties

1. $\varphi(n)$ equals the number of integers in $\{1, 2, \ldots, n-1\}$ coprime to $n$
2. $\varphi(p) = p - 1$ when $p$ is prime
3. $\varphi(n)$ is the order of the multiplicative group $R_n$

# Construction / Recognition

## To Compute:
1. List integers from 1 to $n-1$
2. Count those with $\gcd(m, n) = 1$

# Context & Application

Armstrong introduces $\varphi$ primarily to state Euler's theorem in group-theoretic terms. The phi-function connects the abstract group theory of $R_n$ to classical number theory.

# Examples

**Example 1** (p. 65): $\varphi(9) = 6$ since $R_9 = \{1, 2, 4, 5, 7, 8\}$.

**Example 2** (p. 65): $\varphi(16) = 8$ since $R_{16} = \{1, 3, 5, 7, 9, 11, 13, 15\}$.

# Relationships

## Builds Upon
- **$R_n$ group** — $\varphi(n)$ is defined as the order of $R_n$

## Enables
- **Euler's theorem** — $x^{\varphi(n)} \equiv 1 \pmod{n}$
- **Fermat's little theorem** — Uses $\varphi(p) = p - 1$

# Common Errors

- **Error**: Computing $\varphi(n)$ as $n - 1$ for non-prime $n$
  **Correction**: $\varphi(n) = n - 1$ only when $n$ is prime

# Common Confusions

- **Confusion**: Thinking $\varphi$ is defined only for primes
  **Clarification**: $\varphi(n)$ is defined for all positive integers $n$

# Source Reference

Chapter 11: Lagrange's Theorem, p. 65 (pdf).

# Verification Notes

- Definition source: Direct from p. 65
- Confidence rationale: HIGH — explicitly named and defined
- Uncertainties: None
