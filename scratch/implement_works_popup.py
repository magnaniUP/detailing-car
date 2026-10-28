import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace button in .works-cta-wrapper
old_btn = '''            <div class="works-cta-wrapper">
              <a href="#contatti" class="btn-works-outline" aria-label="Guarda tutti i lavori di detailing eseguiti e richiedi un preventivo">
                <span>Guarda tutti i lavori</span>
                <svg class="btn-works-arrow" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </a>
            </div>'''

new_btn = '''            <div class="works-cta-wrapper">
              <button type="button" 
                      class="btn-works-outline" 
                      id="openWorksModalBtn" 
                      aria-haspopup="dialog" 
                      aria-label="Guarda tutti i lavori di detailing eseguiti e apri la galleria completa">
                <span>Guarda tutti i lavori</span>
                <svg class="btn-works-arrow" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </button>
            </div>'''

if old_btn in html:
    html = html.replace(old_btn, new_btn)
    print('Replaced works CTA button with modal trigger button!')
else:
    print('WARNING: old_btn not found in index.html!')

# Add Works Modal HTML right before </body>
works_modal_html = '''
  <!-- =======================================================================
       POP-UP MODALE: LAVORI ESEGUITI & PORTFOLIO COMPLETO
       Finestra di dialogo modale accessibile e pienamente responsive (Mobile, Tablet, Notebook)
       ======================================================================= -->
  <div class="works-modal-backdrop" id="worksModal" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="worksModalTitle">
    <div class="works-modal-dialog" role="document">
      
      <!-- Testata del Modale con Titolo e Pulsante Chiudi -->
      <div class="works-modal-header">
        <div class="works-modal-header-info">
          <span class="works-modal-eyebrow">PORTFOLIO DETAILING</span>
          <h3 class="works-modal-title" id="worksModalTitle">Tutti i Lavori Conclusi</h3>
          <p class="works-modal-subtitle">Una panoramica completa dei trattamenti esclusivi realizzati dal nostro centro. Cura millimetrica, materiali premium e passione per il risultato.</p>
        </div>
        <button type="button" class="works-modal-close" id="closeWorksModalBtn" aria-label="Chiudi galleria lavori eseguiti">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      </div>

      <!-- Griglia Interattiva dei Lavori Conclusi -->
      <div class="works-modal-body">
        <div class="works-modal-grid">
          
          <!-- Lavoro 1 -->
          <article class="works-modal-card">
            <div class="works-modal-card-media">
              <picture>
                <source srcset="assets/lavoro-1-cerchio.webp?v=4.0" type="image/webp">
                <img src="assets/lavoro-1-cerchio.jpg?v=4.0" alt="Cerchio forgiato nero con pinza dorata" class="works-modal-card-img" width="640" height="384" loading="lazy">
              </picture>
              <span class="works-modal-card-badge">Cerchi & Freni</span>
            </div>
            <div class="works-modal-card-info">
              <h4 class="works-modal-card-title">Cerchio Forgiato & Pinza Oro</h4>
              <p class="works-modal-card-desc">Decontaminazione ferrosa profonda, lucidatura canali e sigillante nanotecnologico ad altissima resistenza termica.</p>
            </div>
          </article>

          <!-- Lavoro 2 -->
          <article class="works-modal-card">
            <div class="works-modal-card-media">
              <picture>
                <source srcset="assets/lavoro-2-interni.webp?v=4.0" type="image/webp">
                <img src="assets/lavoro-2-interni.jpg?v=4.0" alt="Interni in pelle nera con cuciture dorate" class="works-modal-card-img" width="640" height="384" loading="lazy">
              </picture>
              <span class="works-modal-card-badge">Trattamento Pelle</span>
            </div>
            <div class="works-modal-card-info">
              <h4 class="works-modal-card-title">Pelle Nera con Cuciture Artigianali</h4>
              <p class="works-modal-card-desc">Igienizzazione con schiume a pH neutro e nutrimento profondo con balsamo protettivo anti-screpolature.</p>
            </div>
          </article>

          <!-- Lavoro 3 -->
          <article class="works-modal-card">
            <div class="works-modal-card-media">
              <picture>
                <source srcset="assets/lavoro-3-posteriore.webp?v=4.1" type="image/webp">
                <img src="assets/lavoro-3-posteriore.jpg?v=4.1" alt="Posteriore auto premium lucidata" class="works-modal-card-img" width="640" height="384" loading="lazy">
              </picture>
              <span class="works-modal-card-badge">Protezione Ceramica</span>
            </div>
            <div class="works-modal-card-info">
              <h4 class="works-modal-card-title">Coda Premium & Finitura Wet-Look</h4>
              <p class="works-modal-card-desc">Lucidatura di finitura a specchio e applicazione di coating ceramico per una brillantezza e idrofobicità assolute.</p>
            </div>
          </article>

          <!-- Lavoro 4 -->
          <article class="works-modal-card">
            <div class="works-modal-card-media">
              <picture>
                <source srcset="assets/lavoro-4-carrozzeria.webp?v=4.0" type="image/webp">
                <img src="assets/lavoro-4-carrozzeria.jpg?v=4.0" alt="Carrozzeria con riflessi perfetti a specchio" class="works-modal-card-img" width="640" height="384" loading="lazy">
              </picture>
              <span class="works-modal-card-badge">Paint Correction</span>
            </div>
            <div class="works-modal-card-info">
              <h4 class="works-modal-card-title">Carrozzeria a Riflesso Puro</h4>
              <p class="works-modal-card-desc">Correzione in 2 passaggi per eliminare il 95% di swirl e ologrammi, restituendo profondità ottica impeccabile.</p>
            </div>
          </article>

          <!-- Lavoro 5 -->
          <article class="works-modal-card">
            <div class="works-modal-card-media">
              <picture>
                <source srcset="assets/lavoro-5-cerchio.webp?v=4.0" type="image/webp">
                <img src="assets/lavoro-5-cerchio.jpg?v=4.0" alt="Dettaglio finitura cerchio e spalla pneumatico" class="works-modal-card-img" width="640" height="384" loading="lazy">
              </picture>
              <span class="works-modal-card-badge">Dettaglio Ruote</span>
            </div>
            <div class="works-modal-card-info">
              <h4 class="works-modal-card-title">Finitura Ruote & Pneumatici</h4>
              <p class="works-modal-card-desc">Pulizia chimica di precisione e dressing gomme satinato a lunga durata senza effetto unto.</p>
            </div>
          </article>

          <!-- Lavoro 6 -->
          <article class="works-modal-card">
            <div class="works-modal-card-media">
              <picture>
                <source srcset="assets/lavoro-6-interni.webp?v=4.0" type="image/webp">
                <img src="assets/lavoro-6-interni.jpg?v=4.0" alt="Console centrale e tunnel abitacolo" class="works-modal-card-img" width="640" height="384" loading="lazy">
              </picture>
              <span class="works-modal-card-badge">Interni di Lusso</span>
            </div>
            <div class="works-modal-card-info">
              <h4 class="works-modal-card-title">Tunnel Centrale & Plastiche Soft-Touch</h4>
              <p class="works-modal-card-desc">Sanificazione vapore secco a 180°C e schermatura antistatica opaca originale per cruscotto e pulsantiere.</p>
            </div>
          </article>

          <!-- Lavoro 7 -->
          <article class="works-modal-card">
            <div class="works-modal-card-media">
              <picture>
                <source srcset="assets/lavoro-7-faro.webp?v=4.0" type="image/webp">
                <img src="assets/lavoro-7-faro.jpg?v=4.0" alt="Faro a LED trasparente e cristallino" class="works-modal-card-img" width="640" height="384" loading="lazy">
              </picture>
              <span class="works-modal-card-badge">Restauro Fari</span>
            </div>
            <div class="works-modal-card-info">
              <h4 class="works-modal-card-title">Proiettore LED Cristallino</h4>
              <p class="works-modal-card-desc">Rigenerazione del policarbonato con carteggiatura progressiva e sigillatura nanotecnologica anti-UV.</p>
            </div>
          </article>

          <!-- Lavoro 8 -->
          <article class="works-modal-card">
            <div class="works-modal-card-media">
              <picture>
                <source srcset="assets/lavoro-8-finitura.webp?v=4.0" type="image/webp">
                <img src="assets/lavoro-8-finitura.jpg?v=4.0" alt="Dettaglio finitura carrozzeria con perle d'acqua" class="works-modal-card-img" width="640" height="384" loading="lazy">
              </picture>
              <span class="works-modal-card-badge">Coating Nanotech</span>
            </div>
            <div class="works-modal-card-info">
              <h4 class="works-modal-card-title">Effetto Beading & Riflesso Totale</h4>
              <p class="works-modal-card-desc">Tensione superficiale estrema con effetto idrofobico e brillantezza profonda protetta nel tempo.</p>
            </div>
          </article>

        </div>
      </div>

      <!-- Barra Inferiore con CTA WhatsApp per la Galleria -->
      <div class="works-modal-footer">
        <span class="works-modal-footer-note">Vuoi ottenere lo stesso risultato impeccabile per la tua auto?</span>
        <a href="https://wa.me/393911234567?text=Buongiorno%20A.S.%20Top%20Clean!%20Ho%20visto%20i%20vostri%20lavori%20conclusi%20e%20vorrei%20richiedere%20un%20preventivo%20per%20la%20mia%20auto." 
           class="btn-modal-whatsapp" 
           target="_blank" 
           rel="noopener noreferrer"
           aria-label="Richiedi preventivo personalizzato su WhatsApp per la tua auto">
          <svg class="icon-whatsapp" viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true">
            <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2ZM12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.16 12.04 20.16C10.66 20.16 9.3 19.8 8.11 19.1L7.83 18.93L4.71 19.75L5.54 16.71L5.35 16.41C4.55 15.13 4.13 13.54 4.13 11.91C4.13 7.37 7.82 3.67 12.05 3.67ZM8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.7C7.02 10.92 7.91 12.1 8.03 12.26C8.16 12.43 9.77 14.91 12.23 15.97C12.82 16.22 13.27 16.37 13.63 16.49C14.22 16.67 14.76 16.65 15.19 16.59C15.67 16.51 16.66 15.98 16.87 15.4C17.07 14.81 17.07 14.31 17.01 14.21C16.95 14.11 16.79 14.05 16.54 13.92C16.29 13.8 15.08 13.21 14.85 13.13C14.63 13.04 14.46 13 14.3 13.25C14.13 13.49 13.66 14.05 13.52 14.21C13.38 14.38 13.23 14.4 12.99 14.28C12.74 14.16 11.94 13.9 10.99 13.06C10.25 12.4 9.75 11.59 9.61 11.34C9.46 11.1 9.59 10.96 9.72 10.84C9.83 10.73 9.97 10.55 10.09 10.41C10.22 10.27 10.26 10.16 10.34 10C10.42 9.84 10.38 9.7 10.32 9.58C10.26 9.46 9.77 8.25 9.57 7.76C9.37 7.29 9.17 7.35 9.02 7.34C8.87 7.33 8.71 7.33 8.53 7.33Z"/>
          </svg>
          <span>Richiedi preventivo su WhatsApp</span>
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </a>
      </div>

    </div>
  </div>
'''

if 'id="worksModal"' not in html:
    html = html.replace('</body>', works_modal_html + '\n</body>')
    print('Added worksModal HTML before </body>!')

# Bump version to 9.4
html = re.sub(r'css/style\.css\?v=[0-9.]+', 'css/style.css?v=9.4', html)
html = re.sub(r'js/main\.js\?v=[0-9.]+', 'js/main.js?v=9.4', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated successfully with works modal!')


# 2. Update css/style.css: add works modal styles
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

works_modal_css = '''
/* ==========================================================================
   14. MODALE GALLERIA LAVORI ESEGUITI (.works-modal)
   ========================================================================== */

button.btn-works-outline {
  cursor: pointer;
  font: inherit;
}

.works-modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background-color: rgba(4, 7, 10, 0.82);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.28s ease, visibility 0.28s ease;
}

.works-modal-backdrop.is-open {
  opacity: 1;
  visibility: visible;
}

.works-modal-dialog {
  position: relative;
  width: 100%;
  max-width: 960px;
  max-height: 90vh;
  background: #0D151C;
  border: 1px solid rgba(245, 195, 66, 0.25);
  border-radius: 20px;
  box-shadow: 0 28px 72px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.05);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transform: scale(0.95) translateY(12px);
  transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}

.works-modal-backdrop.is-open .works-modal-dialog {
  transform: scale(1) translateY(0);
}

/* Header modale lavori */
.works-modal-header {
  padding: 24px 28px 18px 28px;
  background-color: #070B0E;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 20px;
  flex-shrink: 0;
}

.works-modal-header-info {
  flex: 1;
}

.works-modal-eyebrow {
  display: inline-block;
  font-family: var(--font-primary);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: var(--color-gold);
  text-transform: uppercase;
  margin-bottom: 4px;
}

.works-modal-title {
  font-family: var(--font-brand);
  font-size: 22px;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.01em;
  margin: 0 0 6px 0;
}

.works-modal-subtitle {
  font-family: var(--font-primary);
  font-size: 13px;
  line-height: 1.5;
  color: #94A3B8;
  margin: 0;
  max-width: 720px;
}

.works-modal-close {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-fast);
  flex-shrink: 0;
}

.works-modal-close:hover {
  background: var(--color-gold);
  color: #0D151C;
  border-color: var(--color-gold);
  transform: rotate(90deg);
}

.works-modal-close:focus-visible {
  outline: 2px solid var(--color-gold);
  outline-offset: 2px;
}

/* Corpo modale lavori con griglia */
.works-modal-body {
  padding: 24px 28px;
  overflow-y: auto;
  flex: 1;
}

.works-modal-body::-webkit-scrollbar {
  width: 6px;
}

.works-modal-body::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.04);
}

.works-modal-body::-webkit-scrollbar-thumb {
  background: rgba(245, 195, 66, 0.3);
  border-radius: 3px;
}

.works-modal-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.works-modal-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 14px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform var(--transition-fast), border-color var(--transition-fast), box-shadow var(--transition-fast);
}

.works-modal-card:hover {
  transform: translateY(-3px);
  border-color: rgba(245, 195, 66, 0.4);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}

.works-modal-card-media {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background-color: #070B0E;
}

.works-modal-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.35s ease;
}

.works-modal-card:hover .works-modal-card-img {
  transform: scale(1.05);
}

.works-modal-card-badge {
  position: absolute;
  bottom: 8px;
  left: 8px;
  background: rgba(4, 7, 10, 0.85);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(245, 195, 66, 0.4);
  color: var(--color-gold);
  font-family: var(--font-primary);
  font-size: 10px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 6px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.works-modal-card-info {
  padding: 12px 14px 14px 14px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.works-modal-card-title {
  font-family: var(--font-brand);
  font-size: 13.5px;
  font-weight: 700;
  color: #FFFFFF;
  margin: 0 0 5px 0;
  line-height: 1.35;
}

.works-modal-card-desc {
  font-family: var(--font-primary);
  font-size: 11.5px;
  line-height: 1.45;
  color: #94A3B8;
  margin: 0;
}

/* Footer modale lavori */
.works-modal-footer {
  padding: 18px 28px;
  background-color: #070B0E;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-shrink: 0;
}

.works-modal-footer-note {
  font-family: var(--font-primary);
  font-size: 12px;
  color: #64748B;
  max-width: 380px;
  line-height: 1.4;
}
'''

# Insert base works modal styles before responsive section if not present
if '.works-modal-backdrop' not in css:
    resp_marker = '/* --------------------------------------------------------------------------\n   12. RESPONSIVE DESIGN GLOBALE'
    resp_idx = css.find(resp_marker)
    if resp_idx != -1:
        css = css[:resp_idx] + works_modal_css + '\n' + css[resp_idx:]
    else:
        css += '\n' + works_modal_css
    print('Inserted base works modal CSS into css/style.css!')

# Add responsive works modal styles
# 1. Tablet (1024px)
tablet_works_modal = '''
  /* Works Modal su Tablet (1024px) */
  .works-modal-dialog {
    max-width: 720px;
  }
  .works-modal-header {
    padding: 20px 22px 16px 22px;
  }
  .works-modal-body {
    padding: 20px 22px;
  }
  .works-modal-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }
  .works-modal-footer {
    padding: 16px 22px;
  }'''

if '/* Works Modal su Tablet (1024px) */' not in css:
    target = '/* Modal Servizi su Tablet (1024px) */'
    css = css.replace(target, tablet_works_modal + '\n\n  ' + target)
    print('Added tablet works modal CSS!')

# 2. Mobile (767px)
mobile_works_modal = '''
  /* Works Modal su Mobile (767px) */
  .works-modal-backdrop {
    padding: 12px;
    align-items: flex-end;
  }

  .works-modal-dialog {
    max-width: 100%;
    max-height: 88vh;
    border-radius: 18px 18px 12px 12px;
  }

  .works-modal-header {
    padding: 16px 16px 12px 16px;
  }

  .works-modal-title {
    font-size: 18px;
  }

  .works-modal-subtitle {
    font-size: 12px;
  }

  .works-modal-body {
    padding: 14px 16px;
  }

  .works-modal-grid {
    grid-template-columns: 1fr;
    gap: 14px;
  }

  .works-modal-card-info {
    padding: 10px 12px 12px 12px;
  }

  .works-modal-card-title {
    font-size: 13px;
  }

  .works-modal-footer {
    flex-direction: column;
    align-items: stretch;
    padding: 14px 16px 18px 16px;
    gap: 10px;
  }

  .works-modal-footer-note {
    max-width: 100%;
    text-align: center;
    font-size: 11px;
  }'''

if '/* Works Modal su Mobile (767px) */' not in css:
    target = '/* Modal Servizi su Mobile (767px) */'
    css = css.replace(target, mobile_works_modal + '\n\n  ' + target)
    print('Added mobile works modal CSS!')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('css/style.css updated successfully with works modal styles!')


# 3. Update js/main.js: add initWorksModal and register it
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add initWorksModal to DOMContentLoaded
if 'initWorksModal();' not in js:
    js = js.replace('initWorksGallery();', 'initWorksGallery();\n  initWorksModal();')
    print('Registered initWorksModal in DOMContentLoaded!')

works_js = '''
/**
 * Inizializza il pop-up modale per la galleria di tutti i lavori conclusi
 */
function initWorksModal() {
  const modal = document.getElementById('worksModal');
  const openBtn = document.getElementById('openWorksModalBtn');
  const closeBtn = document.getElementById('closeWorksModalBtn');

  if (!modal || !openBtn) return;

  let lastActiveElement = null;

  function openModal() {
    lastActiveElement = document.activeElement;
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');

    setTimeout(() => {
      if (closeBtn) closeBtn.focus();
    }, 50);
  }

  function closeModal() {
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-open');

    if (lastActiveElement && typeof lastActiveElement.focus === 'function') {
      lastActiveElement.focus();
    }
  }

  openBtn.addEventListener('click', (e) => {
    e.preventDefault();
    openModal();
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  window.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('is-open')) return;

    if (e.key === 'Escape' || e.key === 'Esc') {
      e.preventDefault();
      closeModal();
      return;
    }

    if (e.key === 'Tab') {
      const focusable = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (focusable.length === 0) return;

      const firstEl = focusable[0];
      const lastEl = focusable[focusable.length - 1];

      if (e.shiftKey) {
        if (document.activeElement === firstEl) {
          e.preventDefault();
          lastEl.focus();
        }
      } else {
        if (document.activeElement === lastEl) {
          e.preventDefault();
          firstEl.focus();
        }
      }
    }
  });
}
'''

if 'function initWorksModal()' not in js:
    js += works_js
    print('Appended initWorksModal to js/main.js!')

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('js/main.js updated successfully!')

