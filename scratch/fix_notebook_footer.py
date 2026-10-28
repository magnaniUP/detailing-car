import re

# 1. Update index.html: remove "Perché Sceglierci" from footer nav to match the 6 mockup links
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace footer nav list with exact 6 links from mockup
old_nav_pattern = r'<nav class="footer-nav" aria-label="Navigazione footer">.*?</nav>'
new_nav = '''<nav class="footer-nav" aria-label="Navigazione footer">
          <ul class="footer-nav-list">
            <li class="footer-nav-item">
              <a href="#home" class="footer-nav-link active">Home</a>
            </li>
            <li class="footer-nav-item">
              <a href="#servizi" class="footer-nav-link">Servizi</a>
            </li>
            <li class="footer-nav-item">
              <a href="#lavori" class="footer-nav-link">Lavori Eseguiti</a>
            </li>
            <li class="footer-nav-item">
              <a href="#chi-siamo" class="footer-nav-link">Chi Siamo</a>
            </li>
            <li class="footer-nav-item">
              <a href="#faq" class="footer-nav-link">FAQ</a>
            </li>
            <li class="footer-nav-item">
              <a href="#contatti" class="footer-nav-link">Contatti</a>
            </li>
          </ul>
        </nav>'''

html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)

# Bump version to 9.1
html = re.sub(r'css/style\.css\?v=[0-9.]+', 'css/style.css?v=9.1', html)
html = re.sub(r'js/main\.js\?v=[0-9.]+', 'js/main.js?v=9.1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated successfully with 6 exact mockup links!')


# 2. Update css/style.css: replace footer base styles and responsive styles
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find base footer CSS
footer_start = css.find('/* ==========================================================================\n   12. FOOTER ISTITUZIONALE')
footer_end = css.find('/* --------------------------------------------------------------------------\n   12. RESPONSIVE DESIGN GLOBALE')

if footer_start == -1 or footer_end == -1:
    raise Exception("Footer base CSS markers not found")

new_base_footer = '''/* ==========================================================================
   12. FOOTER ISTITUZIONALE (.site-footer)
   - Layout ultra-premium perfettamente sincronizzato con l'header del mockup
   - Sfondo antracite profondo (#070B0E / #04070A) con contrasto tipografico bilanciato
   - Barra superiore flex orizzontale su tutti i display desktop e notebook:
     Logo a sinistra, 6 link di navigazione al centro, Pulsante CTA a destra
   - Linea divisoria sottile (1px solid rgba(255, 255, 255, 0.08))
   - Barra inferiore: Copyright dinamico e collegamenti Privacy & Cookie Policy
   ========================================================================== */

.site-footer {
  position: relative;
  width: 100%;
  background-color: #070B0E;
  color: #94A3B8;
  padding: 32px 0 22px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
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

css = css[:footer_start] + new_base_footer + css[footer_end:]

# Clean out old responsive footer rules from style.css
css = re.sub(r'  /\* Footer a 1280px \*/.*?\.footer-nav-list \{[^}]*\}\n', '', css, flags=re.DOTALL)
css = re.sub(r'  /\* Footer su Tablet \(1024px\) \*/.*?\.footer-nav-list \{[^}]*\}\n', '', css, flags=re.DOTALL)
css = re.sub(r'  /\* Footer su Mobile \(767px\) \*/.*?\.footer-bottom \{[^}]*\}\n', '', css, flags=re.DOTALL)
css = re.sub(r'  /\* Footer su smartphone compatti \(480px\) \*/.*?\.footer-legal-link \{[^}]*\}\n', '', css, flags=re.DOTALL)
css = re.sub(r'  /\* Footer su smartphone molto piccoli \(360px\) \*/.*?\.footer-container \{[^}]*\}\n', '', css, flags=re.DOTALL)

# Add optimized responsive rules
# 1. Notebooks / Laptops (1025px - 1280px)
css = css.replace(
    '/* Contatti a 1280px */\n  .contact-container {\n    padding: 0 32px;\n  }\n\n  .contact-layout {\n    grid-template-columns: minmax(240px, 1fr) minmax(340px, 1.35fr) minmax(190px, 0.85fr);\n    gap: 28px;\n  }',
    '/* Contatti a 1280px */\n  .contact-container {\n    padding: 0 32px;\n  }\n\n  .contact-layout {\n    grid-template-columns: minmax(240px, 1fr) minmax(340px, 1.35fr) minmax(190px, 0.85fr);\n    gap: 28px;\n  }\n\n  /* Footer su Notebook (1280px) */\n  .site-footer {\n    padding: 28px 0 18px 0;\n  }\n\n  .footer-container {\n    padding: 0 24px;\n  }\n\n  .footer-main {\n    padding-bottom: 20px;\n    gap: 16px;\n  }\n\n  .footer-logo {\n    height: 36px;\n  }\n\n  .footer-nav-list {\n    gap: 20px;\n  }\n\n  .footer-nav-link {\n    font-size: 12.5px;\n  }\n\n  .btn-footer-contact {\n    padding: 7px 15px;\n    font-size: 12px;\n  }\n\n  .footer-divider {\n    margin: 0 0 16px 0;\n  }\n\n  .footer-bottom {\n    font-size: 11.5px;\n  }'
)

# 2. Notebooks compatti / Tablets landscape (768px - 1024px)
css = css.replace(
    '/* Contatti su Tablet (1024px) */\n  .contact-section {\n    padding: 56px 0 64px 0;\n  }\n\n  .contact-container {\n    padding: 0 24px;\n  }\n\n  .contact-layout {\n    grid-template-columns: 1fr;\n    gap: 32px;\n  }\n\n  .contact-intro-col {\n    max-width: 650px;\n  }\n\n  .contact-bg-ambient {\n    width: 100%;\n    opacity: 0.16;\n  }',
    '/* Contatti su Tablet (1024px) */\n  .contact-section {\n    padding: 56px 0 64px 0;\n  }\n\n  .contact-container {\n    padding: 0 24px;\n  }\n\n  .contact-layout {\n    grid-template-columns: 1fr;\n    gap: 32px;\n  }\n\n  .contact-intro-col {\n    max-width: 650px;\n  }\n\n  .contact-bg-ambient {\n    width: 100%;\n    opacity: 0.16;\n  }\n\n  /* Footer su Tablet e Notebook compatto (1024px) - Mantiene composizione orizzontale pulita */\n  .site-footer {\n    padding: 24px 0 16px 0;\n  }\n\n  .footer-container {\n    padding: 0 20px;\n  }\n\n  .footer-main {\n    display: flex;\n    flex-direction: row;\n    align-items: center;\n    justify-content: space-between;\n    gap: 12px;\n    padding-bottom: 18px;\n  }\n\n  .footer-logo {\n    height: 32px;\n  }\n\n  .footer-nav-list {\n    gap: 14px;\n  }\n\n  .footer-nav-link {\n    font-size: 12px;\n  }\n\n  .btn-footer-contact {\n    padding: 6.5px 13px;\n    font-size: 11.5px;\n    gap: 5px;\n  }\n\n  .btn-footer-contact .btn-arrow {\n    display: none;\n  }\n\n  .footer-divider {\n    margin: 0 0 14px 0;\n  }\n\n  .footer-bottom {\n    display: flex;\n    flex-direction: row;\n    justify-content: space-between;\n    align-items: center;\n    font-size: 11px;\n  }'
)

# 3. Mobile (767px)
css = css.replace(
    '  .contact-social-icons {\n    display: flex;\n    align-items: center;\n    justify-content: flex-start;\n    gap: 10px;\n  }\n}',
    '  .contact-social-icons {\n    display: flex;\n    align-items: center;\n    justify-content: flex-start;\n    gap: 10px;\n  }\n\n  /* Footer su Mobile (767px) */\n  .site-footer {\n    padding: 34px 0 24px 0;\n  }\n\n  .footer-container {\n    padding: 0 16px;\n  }\n\n  .footer-main {\n    flex-direction: column;\n    align-items: center;\n    text-align: center;\n    gap: 20px;\n    padding-bottom: 22px;\n  }\n\n  .footer-logo {\n    height: 36px;\n  }\n\n  .footer-nav-list {\n    flex-direction: column;\n    gap: 12px;\n    width: 100%;\n    flex-wrap: wrap;\n  }\n\n  .footer-nav-link {\n    display: block;\n    font-size: 13.5px;\n    padding: 4px 0;\n  }\n\n  .footer-actions {\n    width: 100%;\n    display: flex;\n    justify-content: center;\n  }\n\n  .btn-footer-contact {\n    width: 100%;\n    max-width: 260px;\n    padding: 10px 18px;\n    font-size: 13px;\n  }\n\n  .btn-footer-contact .btn-arrow {\n    display: inline-block;\n  }\n\n  .footer-divider {\n    margin: 0 0 16px 0;\n  }\n\n  .footer-bottom {\n    flex-direction: column;\n    align-items: center;\n    text-align: center;\n    gap: 10px;\n    font-size: 11.5px;\n  }\n}'
)

# 4. Smartphone compact (480px)
css = css.replace(
    '/* Contatti su smartphone compatti (480px) */\n  .contact-section {\n    padding: 40px 0 46px 0;\n  }\n\n  .contact-heading {\n    font-size: 20px;\n  }\n\n  .contact-input {\n    padding: 8.5px 11px;\n    font-size: 12.5px;\n  }',
    '/* Contatti su smartphone compatti (480px) */\n  .contact-section {\n    padding: 40px 0 46px 0;\n  }\n\n  .contact-heading {\n    font-size: 20px;\n  }\n\n  .contact-input {\n    padding: 8.5px 11px;\n    font-size: 12.5px;\n  }\n\n  /* Footer su smartphone compatti (480px) */\n  .footer-container {\n    padding: 0 14px;\n  }\n\n  .footer-copyright {\n    font-size: 11px;\n  }\n\n  .footer-legal-link {\n    font-size: 11px;\n  }'
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('css/style.css updated successfully with notebook fixes!')

