import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add .sr-only utility to CSS if missing
if '.sr-only' not in css:
    sr_only_css = '''/* Accessibility Utility: Screen Reader Only */
.sr-only {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
}

'''
    # Insert right at the top after reset or root
    root_idx = css.find(':root {')
    if root_idx != -1:
        css = css[:root_idx] + sr_only_css + css[root_idx:]
    else:
        css = sr_only_css + css

# 2. Update base .site-footer styles (Desktop 1281px+)
# Replace base footer CSS
footer_base_start = css.find('/* ==========================================================================\n   12. FOOTER ISTITUZIONALE')
footer_base_end = css.find('/* --------------------------------------------------------------------------\n   12. RESPONSIVE DESIGN GLOBALE')

if footer_base_start == -1 or footer_base_end == -1:
    raise Exception("Footer base CSS markers not found")

new_base_footer = '''/* ==========================================================================
   12. FOOTER ISTITUZIONALE (.site-footer)
   - Layout ultra-premium perfettamente sincronizzato con l'header del mockup
   - Desktop (1281px+): Logo a sinistra, 6 link centrali, Pulsante CTA a destra
   - Tablet (768px – 1024px): Composizione bilanciata a 3 livelli centrati
   - Mobile (< 768px): Struttura verticale elegante senza overflow
   ========================================================================== */

.site-footer {
  position: relative;
  width: 100%;
  background-color: #070B0E;
  color: #94A3B8;
  padding: 32px 0 22px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.site-footer .sr-only {
  display: none !important;
}

.footer-container {
  width: 100%;
  max-width: var(--container-max-width);
  margin: 0 auto;
  padding: 0 24px;
}

.footer-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 24px;
  gap: 20px;
}

.footer-logo-link {
  display: inline-flex;
  align-items: center;
  text-decoration: none;
  flex-shrink: 0;
  transition: opacity var(--transition-fast);
}

.footer-logo-link:hover {
  opacity: 0.88;
}

.footer-logo {
  height: 38px;
  width: auto;
  display: block;
}

/* Navigazione centrale */
.footer-nav {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
}

.footer-nav-list {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 28px;
  list-style: none;
  padding: 0;
  margin: 0;
  flex-wrap: nowrap;
}

.footer-nav-item {
  display: inline-flex;
  align-items: center;
}

.footer-nav-link {
  font-family: var(--font-primary);
  font-size: 13px;
  font-weight: 500;
  color: #94A3B8;
  text-decoration: none;
  position: relative;
  transition: color var(--transition-fast);
  padding: 4px 0;
  white-space: nowrap;
}

.footer-nav-link:hover,
.footer-nav-link.active {
  color: var(--color-gold);
}

.footer-nav-link:focus-visible {
  outline: 2px solid var(--color-gold);
  outline-offset: 4px;
  border-radius: 2px;
}

/* Pulsante CTA Destra */
.footer-actions {
  flex-shrink: 0;
  display: flex;
  align-items: center;
}

.btn-footer-contact {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  padding: 8px 18px;
  background-color: var(--color-gold);
  color: #0D151C;
  border-radius: 9999px;
  font-family: var(--font-primary);
  font-size: 12.5px;
  font-weight: 700;
  text-decoration: none;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), filter var(--transition-fast);
  box-shadow: 0 2px 10px rgba(245, 195, 66, 0.25);
  cursor: pointer;
  border: none;
  white-space: nowrap;
}

.btn-footer-contact:hover {
  transform: translateY(-2px);
  filter: brightness(1.06);
  box-shadow: 0 4px 14px rgba(245, 195, 66, 0.38);
  color: #0D151C;
}

.btn-footer-contact:focus-visible {
  outline: 2px solid #FFFFFF;
  outline-offset: 3px;
}

/* Linea divisoria */
.footer-divider {
  width: 100%;
  height: 1px;
  background-color: rgba(255, 255, 255, 0.08);
  margin: 0 0 18px 0;
}

/* Barra inferiore */
.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: var(--font-primary);
  font-size: 12px;
  color: #64748B;
  flex-wrap: nowrap;
}

.footer-copyright {
  margin: 0;
  color: #64748B;
  white-space: nowrap;
}

.footer-legal-links {
  display: flex;
  align-items: center;
  gap: 12px;
  white-space: nowrap;
}

.footer-legal-link {
  color: #64748B;
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-legal-link:hover {
  color: var(--color-gold);
}

.footer-legal-link:focus-visible {
  outline: 1px solid var(--color-gold);
  outline-offset: 2px;
}

.legal-separator {
  color: #334155;
  font-size: 11px;
}

'''

css = css[:footer_base_start] + new_base_footer + css[footer_base_end:]

# 3. Clean any existing footer responsive rules
css = re.sub(r'  /\* Footer su Notebook \(1280px\) \*/.*?\.footer-bottom \{[^}]*\}\n', '', css, flags=re.DOTALL)
css = re.sub(r'  /\* Footer su Tablet e Notebook compatto \(1024px\) - Mantiene composizione orizzontale pulita \*/.*?\.footer-bottom \{[^}]*\}\n', '', css, flags=re.DOTALL)
css = re.sub(r'  /\* Footer su Tablet \(1024px\) \*/.*?\.footer-bottom \{[^}]*\}\n', '', css, flags=re.DOTALL)
css = re.sub(r'  /\* Footer su Mobile \(767px\) \*/.*?\.footer-bottom \{[^}]*\}\n', '', css, flags=re.DOTALL)
css = re.sub(r'  /\* Footer su smartphone compatti \(480px\) \*/.*?\.footer-legal-link \{[^}]*\}\n', '', css, flags=re.DOTALL)
css = re.sub(r'  /\* Footer su smartphone molto piccoli \(360px\) \*/.*?\.footer-container \{[^}]*\}\n', '', css, flags=re.DOTALL)

# 4. Insert responsive rule for 1280px (Notebook)
css = css.replace(
    '/* Contatti a 1280px */\n  .contact-container {\n    padding: 0 32px;\n  }\n\n  .contact-layout {\n    grid-template-columns: minmax(240px, 1fr) minmax(340px, 1.35fr) minmax(190px, 0.85fr);\n    gap: 28px;\n  }',
    '''/* Contatti a 1280px */
  .contact-container {
    padding: 0 32px;
  }

  .contact-layout {
    grid-template-columns: minmax(240px, 1fr) minmax(340px, 1.35fr) minmax(190px, 0.85fr);\n    gap: 28px;
  }

  /* Footer su Notebook (1280px) */
  .site-footer {
    padding: 28px 0 18px 0;
  }

  .footer-container {
    padding: 0 24px;
  }

  .footer-main {
    padding-bottom: 20px;
    gap: 16px;
  }

  .footer-logo {
    height: 36px;
  }

  .footer-nav-list {
    gap: 20px;
  }

  .footer-nav-link {
    font-size: 12.5px;
  }

  .btn-footer-contact {
    padding: 7px 15px;
    font-size: 12px;
  }

  .footer-divider {
    margin: 0 0 16px 0;
  }

  .footer-bottom {
    font-size: 11.5px;
  }'''
)

# 5. Insert responsive rule for 1024px (Tablet)
css = css.replace(
    '/* Contatti su Tablet (1024px) */\n  .contact-section {\n    padding: 56px 0 64px 0;\n  }\n\n  .contact-container {\n    padding: 0 24px;\n  }\n\n  .contact-layout {\n    grid-template-columns: 1fr;\n    gap: 32px;\n  }\n\n  .contact-intro-col {\n    max-width: 650px;\n  }\n\n  .contact-bg-ambient {\n    width: 100%;\n    opacity: 0.16;\n  }',
    '''/* Contatti su Tablet (1024px) */
  .contact-section {
    padding: 56px 0 64px 0;
  }

  .contact-container {
    padding: 0 24px;
  }

  .contact-layout {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .contact-intro-col {
    max-width: 650px;
  }

  .contact-bg-ambient {
    width: 100%;
    opacity: 0.16;
  }

  /* Footer su Tablet (1024px) - Layout elegante a 3 livelli centrati */
  .site-footer {
    padding: 32px 0 22px 0;
  }

  .footer-container {
    padding: 0 24px;
  }

  .footer-main {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 18px;
    padding-bottom: 20px;
  }

  .footer-logo {
    height: 36px;
  }

  .footer-nav {
    width: 100%;
  }

  .footer-nav-list {
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px 24px;
  }

  .footer-nav-link {
    font-size: 13px;
    padding: 4px 6px;
  }

  .footer-actions {
    display: flex;
    justify-content: center;
    width: 100%;
  }

  .btn-footer-contact {
    padding: 8px 18px;
    font-size: 12.5px;
  }

  .footer-divider {
    margin: 0 0 16px 0;
  }

  .footer-bottom {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    font-size: 11.5px;
    white-space: normal;
  }'''
)

# 6. Insert responsive rule for 767px (Mobile)
# Target contact-social-icons inside 767px media query
target_767 = '''  .contact-social-icons {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 10px;
  }'''

replacement_767 = '''  .contact-social-icons {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 10px;
  }

  /* Footer su Mobile (767px) - Layout verticale ordinato conforme al mockup */
  .site-footer {
    padding: 36px 0 24px 0;
  }

  .footer-container {
    padding: 0 16px;
  }

  .footer-main {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 20px;
    padding-bottom: 22px;
  }

  .footer-logo {
    height: 38px;
  }

  .footer-nav {
    width: 100%;
  }

  .footer-nav-list {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    width: 100%;
    flex-wrap: wrap;
  }

  .footer-nav-link {
    display: inline-block;
    font-size: 14px;
    color: #CBD5E1;
    padding: 5px 12px;
    white-space: normal;
  }

  .footer-actions {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 4px;
  }

  .btn-footer-contact {
    width: 100%;
    max-width: 250px;
    padding: 10px 18px;
    font-size: 13px;
    justify-content: center;
  }

  .btn-footer-contact .btn-arrow {
    display: inline-block;
  }

  .footer-divider {
    margin: 0 0 16px 0;
  }

  .footer-bottom {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 10px;
    font-size: 11.5px;
    white-space: normal;
  }

  .footer-copyright {
    white-space: normal;
    line-height: 1.5;
  }

  .footer-legal-links {
    justify-content: center;
    gap: 12px;
    white-space: normal;
  }'''

if target_767 in css:
    css = css.replace(target_767, replacement_767)
else:
    raise Exception("Target 767px contact-social-icons not found in style.css")

# 7. Insert responsive rule for 480px (Smartphone compatti)
target_480 = '''/* Contatti su smartphone compatti (480px) */
  .contact-section {
    padding: 40px 0 46px 0;
  }

  .contact-heading {
    font-size: 20px;
  }

  .contact-input {
    padding: 8.5px 11px;
    font-size: 12.5px;
  }'''

replacement_480 = '''/* Contatti su smartphone compatti (480px) */
  .contact-section {
    padding: 40px 0 46px 0;
  }

  .contact-heading {
    font-size: 20px;
  }

  .contact-input {
    padding: 8.5px 11px;
    font-size: 12.5px;
  }

  /* Footer su smartphone compatti (480px) */
  .footer-container {
    padding: 0 14px;
  }

  .footer-logo {
    height: 34px;
  }

  .footer-nav-link {
    font-size: 13.5px;
  }

  .btn-footer-contact {
    max-width: 240px;
  }

  .footer-copyright {
    font-size: 11px;
  }

  .footer-legal-link {
    font-size: 11px;
  }'''

if target_480 in css:
    css = css.replace(target_480, replacement_480)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('css/style.css updated successfully with complete mobile & tablet footer rules!')

# 8. Bump version in index.html to 9.2
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'css/style\.css\?v=[0-9.]+', 'css/style.css?v=9.2', html)
html = re.sub(r'js/main\.js\?v=[0-9.]+', 'js/main.js?v=9.2', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html version bumped to 9.2!')

