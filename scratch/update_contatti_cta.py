import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- =======================================================================\n         FASE 8 — SEZIONE CONTATTI'
end_marker = '</section>'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx) + len(end_marker)

new_html_section = '''<!-- =======================================================================
         FASE 8 — SEZIONE CONTATTI & PRENOTAZIONE WHATSAPP (ID: #contatti)
         Riproduzione fedele del mockup con pulsante CTA WhatsApp dedicato:
         - Colonna 1: Eyebrow dorato "CONTATTI", Titolo e descrizione del servizio
         - Colonna 2: Box CTA WhatsApp diretto per prenotazione rapida
         - Colonna 3: Info dirette (+39 391 123 4567, info@astopclean.it, Via Roma 123 Milano, Italia) e social
         - Sfondo ambiente car studio sul lato destro
         ======================================================================= -->
    <section id="contatti" class="contact-section" aria-labelledby="contact-heading">
      <!-- Immagine di sfondo ambiente studio con auto scura sul lato destro -->
      <div class="contact-bg-ambient" aria-hidden="true">
        <picture>
          <source srcset="assets/contatti-car-ambient.webp?v=8.3" type="image/webp">
          <img src="assets/contatti-car-ambient.jpg?v=8.3" 
               alt="" 
               class="contact-ambient-img"
               loading="lazy" 
               width="1400" 
               height="1303">
        </picture>
        <div class="contact-bg-overlay"></div>
      </div>

      <div class="contact-container">
        <div class="contact-layout">

          <!-- COLONNA 1: INTRODUZIONE (SINISTRA) -->
          <div class="contact-intro-col">
            <span class="contact-eyebrow">CONTATTI</span>
            <h2 id="contact-heading" class="contact-heading">
              Richiedi un preventivo o prenota il tuo trattamento
            </h2>
            <p class="contact-description">
              Siamo a tua disposizione per qualsiasi informazione o per fissare un appuntamento. Contattaci direttamente su WhatsApp, ti risponderemo al più presto.
            </p>
          </div>

          <!-- COLONNA 2: BOX CTA WHATSAPP (CENTRO) -->
          <div class="contact-cta-col">
            <div class="contact-cta-box">
              <span class="contact-cta-eyebrow">PRENOTAZIONE RAPIDA</span>
              <p class="contact-cta-lead">
                Fissa il tuo lavaggio o richiedi un preventivo personalizzato direttamente su WhatsApp.
              </p>
              <a href="https://wa.me/393911234567?text=Buongiorno%20A.S.%20Top%20Clean!%20Vorrei%20prenotare%20un%20lavaggio%20o%20trattamento%20per%20la%20mia%20auto." 
                 id="contactWhatsAppCta" 
                 class="btn-contact-whatsapp" 
                 target="_blank" 
                 rel="noopener noreferrer" 
                 aria-label="Prenota o richiedi informazioni su WhatsApp">
                <span class="btn-wa-icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">
                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                  </svg>
                </span>
                <span class="btn-wa-text">Prenota su WhatsApp</span>
                <span class="btn-wa-arrow" aria-hidden="true">→</span>
              </a>
              <span class="contact-cta-hint">Risposta rapida durante gli orari di apertura del centro</span>
            </div>
          </div>

          <!-- COLONNA 3: INFO DI CONTATTO & SOCIAL (DESTRA) -->
          <div class="contact-info-col">
            <div class="contact-direct-items">
              <!-- Telefono -->
              <a href="tel:+393911234567" class="contact-direct-item" aria-label="Telefono: +39 391 123 4567">
                <span class="contact-info-icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                  </svg>
                </span>
                <span class="contact-info-text">+39 391 123 4567</span>
              </a>

              <!-- Email -->
              <a href="mailto:info@astopclean.it" class="contact-direct-item" aria-label="Email: info@astopclean.it">
                <span class="contact-info-icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                    <polyline points="22,6 12,13 2,6"></polyline>
                  </svg>
                </span>
                <span class="contact-info-text">info@astopclean.it</span>
              </a>

              <!-- Indirizzo -->
              <div class="contact-direct-item contact-address-item">
                <span class="contact-info-icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                    <circle cx="12" cy="10" r="3"></circle>
                  </svg>
                </span>
                <span class="contact-info-text">
                  Via Roma 123<br>Milano, Italia
                </span>
              </div>
            </div>

            <!-- Social Links -->
            <div class="contact-social-group">
              <span class="contact-social-label">Seguici sui social</span>
              <div class="contact-social-icons">
                <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="social-icon-box" aria-label="Seguici su Instagram">
                  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                    <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                    <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                  </svg>
                </a>
                <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" class="social-icon-box" aria-label="Seguici su Facebook">
                  <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                  </svg>
                </a>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>'''

html = html[:start_idx] + new_html_section + html[end_idx:]
html = re.sub(r'css/style\.css\?v=[0-9.]+', 'css/style.css?v=8.3', html)
html = re.sub(r'js/main\.js\?v=[0-9.]+', 'js/main.js?v=8.3', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated successfully!')

# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

s_marker = '/* ==========================================================================\n   11. SEZIONE CONTATTI E RICHIESTA PREVENTIVO'
e_marker = '/* --------------------------------------------------------------------------\n   12. RESPONSIVE DESIGN'

s_idx = css.find(s_marker)
e_idx = css.find(e_marker)

new_base_css = '''/* ==========================================================================
   11. SEZIONE CONTATTI & PRENOTAZIONE WHATSAPP (#contatti)
   - Layout orizzontale a 3 colonne su sfondo nero antracite (#070D12)
   - Colonna 1: Eyebrow dorato "CONTATTI", Titolo e descrizione del servizio
   - Colonna 2: Box CTA WhatsApp per prenotazione rapida
   - Colonna 3: Info dirette (+39 391 123 4567, info@astopclean.it, Via Roma 123 Milano) e social
   - Sfondo ambiente car studio sul lato destro
   ========================================================================== */

.contact-section {
  position: relative;
  width: 100%;
  background-color: #070D12;
  color: #FFFFFF;
  padding: 68px 0 76px 0;
  overflow: hidden;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

/* Sfondo ambiente studio con auto scura sul lato destro */
.contact-bg-ambient {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 48%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
  overflow: hidden;
}

.contact-ambient-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center right;
  opacity: 0.36;
  filter: contrast(1.15) brightness(0.85);
}

.contact-bg-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to right,
    #070D12 0%,
    rgba(7, 13, 18, 0.95) 20%,
    rgba(7, 13, 18, 0.75) 55%,
    rgba(7, 13, 18, 0.25) 100%
  ),
  linear-gradient(
    to bottom,
    #070D12 0%,
    transparent 15%,
    transparent 85%,
    #070D12 100%
  );
}

.contact-container {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: var(--container-max-width);
  margin: 0 auto;
  padding: 0 40px;
}

/* Layout a 3 colonne affiancate su desktop */
.contact-layout {
  display: grid;
  grid-template-columns: minmax(260px, 1.05fr) minmax(360px, 1.35fr) minmax(210px, 0.85fr);
  gap: 40px;
  align-items: center;
}

/* COLONNA 1: INTRODUZIONE */
.contact-intro-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.contact-eyebrow {
  display: inline-block;
  font-family: var(--font-primary);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--color-gold);
  margin-bottom: 12px;
}

.contact-heading {
  font-family: var(--font-brand);
  font-size: clamp(22px, 1.85vw, 26px);
  font-weight: 800;
  line-height: 1.22;
  letter-spacing: -0.02em;
  color: #FFFFFF;
  margin-bottom: 14px;
}

.contact-description {
  font-family: var(--font-primary);
  font-size: 13px;
  line-height: 1.62;
  color: #94A3B8;
  margin: 0;
}

/* COLONNA 2: BOX CTA WHATSAPP (IN LUOGO DEL FORM) */
.contact-cta-col {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
}

.contact-cta-box {
  background: rgba(9, 18, 24, 0.78);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 24px 28px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
  box-shadow: 0 12px 28px -6px rgba(0, 0, 0, 0.4);
  position: relative;
}

.contact-cta-box::before {
  content: '';
  position: absolute;
  top: 0;
  left: 24px;
  right: 24px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--color-gold), transparent);
  opacity: 0.7;
}

.contact-cta-eyebrow {
  font-family: var(--font-primary);
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: var(--color-gold);
  text-transform: uppercase;
}

.contact-cta-lead {
  font-family: var(--font-primary);
  font-size: 13.5px;
  line-height: 1.55;
  color: #E2E8F0;
  margin: 0;
}

.btn-contact-whatsapp {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: auto;
  min-width: 240px;
  padding: 13px 26px;
  background: var(--color-gold);
  color: #0D151C;
  border: none;
  border-radius: 9999px;
  font-family: var(--font-primary);
  font-size: 14.5px;
  font-weight: 800;
  letter-spacing: -0.01em;
  text-decoration: none;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(245, 195, 66, 0.32);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), filter var(--transition-fast);
  margin-top: 4px;
}

.btn-contact-whatsapp:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(245, 195, 66, 0.45);
  filter: brightness(1.05);
  color: #0D151C;
}

.btn-contact-whatsapp:focus-visible {
  outline: 3px solid #FFFFFF;
  outline-offset: 2px;
}

.btn-contact-whatsapp .btn-wa-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #0D151C;
}

.btn-contact-whatsapp .btn-wa-arrow {
  font-size: 16px;
  transition: transform var(--transition-fast);
}

.btn-contact-whatsapp:hover .btn-wa-arrow {
  transform: translateX(4px);
}

.contact-cta-hint {
  font-size: 11.5px;
  color: #64748B;
  line-height: 1.4;
  margin-top: 2px;
}

/* COLONNA 3: INFO DI CONTATTO & SOCIAL */
.contact-info-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.contact-direct-items {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.contact-direct-item {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #E2E8F0;
  text-decoration: none;
  font-family: var(--font-primary);
  font-size: 13px;
  font-weight: 500;
  transition: color var(--transition-fast);
}

.contact-direct-item:hover {
  color: var(--color-gold);
}

.contact-address-item {
  align-items: flex-start;
}

.contact-info-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  color: var(--color-gold);
  flex-shrink: 0;
  margin-top: 1px;
}

.contact-info-text {
  line-height: 1.45;
}

/* Social links */
.contact-social-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 2px;
}

.contact-social-label {
  font-family: var(--font-primary);
  font-size: 12px;
  color: #94A3B8;
  font-weight: 500;
}

.contact-social-icons {
  display: flex;
  align-items: center;
  gap: 10px;
}

.social-icon-box {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border: 1.5px solid rgba(255, 255, 255, 0.45);
  border-radius: 6px;
  color: #FFFFFF;
  text-decoration: none;
  transition: all var(--transition-fast);
}

.social-icon-box:hover {
  border-color: var(--color-gold);
  color: var(--color-gold);
  transform: translateY(-2px);
}
'''

css = css[:s_idx] + new_base_css + '\n' + css[e_idx:]
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('css/style.css updated successfully!')

# 3. Update js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update DOMContentLoaded
js = js.replace('initContactForm();', 'initContactWhatsApp();')

# Replace initContactForm with initContactWhatsApp
js_func_marker = '/**\n * Inizializza il modulo di richiesta'
idx_js = js.find(js_func_marker)
if idx_js != -1:
    new_js_func = '''/**
 * Inizializza il collegamento dinamico del pulsante WhatsApp nella sezione Contatti
 */
function initContactWhatsApp() {
  const ctaBtn = document.getElementById('contactWhatsAppCta');
  if (!ctaBtn) return;

  ctaBtn.addEventListener('click', (e) => {
    const phoneClean = COMPANY_CONFIG.whatsappPhone.replace(/[^0-9]/g, '');
    if (phoneClean.length >= 8) {
      e.preventDefault();
      const encodedMsg = encodeURIComponent(COMPANY_CONFIG.defaultMessage);
      const waUrl = `https://wa.me/${phoneClean}?text=${encodedMsg}`;
      window.open(waUrl, '_blank', 'noopener,noreferrer');
    }
  });
}
'''
    js = js[:idx_js] + new_js_func

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('js/main.js updated successfully!')

