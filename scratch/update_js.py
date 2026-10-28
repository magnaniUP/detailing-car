code = """/**
 * Inizializza il modulo di richiesta preventivo / contatto (#contactForm)
 * Valida i campi obbligatori (Nome, Email, Telefono, Servizio)
 * e apre WhatsApp con il messaggio precompilato o fornisce feedback di conferma.
 */
function initContactForm() {
  const form = document.getElementById("contactForm");
  const statusBanner = document.getElementById("contactFormStatus");
  if (!form) return;

  const nameInput = document.getElementById("contactName");
  const emailInput = document.getElementById("contactEmail");
  const phoneInput = document.getElementById("contactPhone");
  const serviceInput = document.getElementById("contactService");
  const messageInput = document.getElementById("contactMessage");

  const nameError = document.getElementById("contactNameError");
  const emailError = document.getElementById("contactEmailError");
  const phoneError = document.getElementById("contactPhoneError");
  const serviceError = document.getElementById("contactServiceError");

  // Rimuove gli errori visivi durante la digitazione
  [nameInput, emailInput, phoneInput, serviceInput].forEach(field => {
    if (!field) return;
    const eventName = field.tagName === "SELECT" ? "change" : "input";
    field.addEventListener(eventName, () => {
      field.classList.remove("is-invalid");
      field.removeAttribute("aria-invalid");
      const errEl = document.getElementById(field.id + "Error");
      if (errEl) errEl.textContent = "";
      if (statusBanner && statusBanner.classList.contains("is-error")) {
        statusBanner.style.display = "none";
      }
    });
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    let isValid = true;
    let firstInvalidField = null;

    // 1. Validazione Nome (Obbligatorio)
    const nameVal = nameInput ? nameInput.value.trim() : "";
    if (!nameVal || nameVal.length < 2) {
      isValid = false;
      if (nameInput) {
        nameInput.classList.add("is-invalid");
        nameInput.setAttribute("aria-invalid", "true");
        if (!firstInvalidField) firstInvalidField = nameInput;
      }
      if (nameError) nameError.textContent = "Inserisci nome e cognome.";
    } else {
      if (nameInput) {
        nameInput.classList.remove("is-invalid");
        nameInput.removeAttribute("aria-invalid");
      }
      if (nameError) nameError.textContent = "";
    }

    // 2. Validazione Email (Obbligatorio)
    const emailVal = emailInput ? emailInput.value.trim() : "";
    const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
    if (!emailVal || !emailRegex.test(emailVal)) {
      isValid = false;
      if (emailInput) {
        emailInput.classList.add("is-invalid");
        emailInput.setAttribute("aria-invalid", "true");
        if (!firstInvalidField) firstInvalidField = emailInput;
      }
      if (emailError) emailError.textContent = "Inserisci un indirizzo email valido.";
    } else {
      if (emailInput) {
        emailInput.classList.remove("is-invalid");
        emailInput.removeAttribute("aria-invalid");
      }
      if (emailError) emailError.textContent = "";
    }

    // 3. Validazione Telefono (Obbligatorio)
    const phoneVal = phoneInput ? phoneInput.value.trim() : "";
    const phoneDigits = phoneVal.replace(/[^0-9]/g, "");
    if (!phoneVal || phoneDigits.length < 7) {
      isValid = false;
      if (phoneInput) {
        phoneInput.classList.add("is-invalid");
        phoneInput.setAttribute("aria-invalid", "true");
        if (!firstInvalidField) firstInvalidField = phoneInput;
      }
      if (phoneError) phoneError.textContent = "Inserisci un recapito valido.";
    } else {
      if (phoneInput) {
        phoneInput.classList.remove("is-invalid");
        phoneInput.removeAttribute("aria-invalid");
      }
      if (phoneError) phoneError.textContent = "";
    }

    // 4. Validazione Servizio (Obbligatorio)
    const serviceVal = serviceInput ? serviceInput.value.trim() : "";
    if (!serviceVal) {
      isValid = false;
      if (serviceInput) {
        serviceInput.classList.add("is-invalid");
        serviceInput.setAttribute("aria-invalid", "true");
        if (!firstInvalidField) firstInvalidField = serviceInput;
      }
      if (serviceError) serviceError.textContent = "Seleziona un servizio.";
    } else {
      if (serviceInput) {
        serviceInput.classList.remove("is-invalid");
        serviceInput.removeAttribute("aria-invalid");
      }
      if (serviceError) serviceError.textContent = "";
    }

    if (!isValid) {
      if (firstInvalidField) firstInvalidField.focus();
      return;
    }

    // Messaggio facoltativo
    const messageVal = messageInput ? messageInput.value.trim() : "";

    // Costruzione messaggio WhatsApp precompilato
    let waMessage = "🚗 *RICHIESTA PREVENTIVO — A.S. TOP CLEAN*\\n\\n";
    waMessage += "👤 *Nome e Cognome:* " + nameVal + "\\n";
    waMessage += "📧 *Email:* " + emailVal + "\\n";
    waMessage += "📞 *Telefono:* " + phoneVal + "\\n";
    waMessage += "🛠️ *Servizio:* " + serviceVal + "\\n";
    if (messageVal) {
      waMessage += "💬 *Messaggio:* " + messageVal + "\\n";
    }
    waMessage += "\\nRichiesta inviata dal sito web astopclean.it";

    const phoneClean = COMPANY_CONFIG.whatsappPhone.replace(/[^0-9]/g, "");

    if (phoneClean.length >= 8) {
      const waUrl = "https://wa.me/" + phoneClean + "?text=" + encodeURIComponent(waMessage);
      if (statusBanner) {
        statusBanner.className = "contact-status-banner is-success";
        statusBanner.innerHTML = "<strong>Grazie " + nameVal + "!</strong> Stiamo aprendo WhatsApp per completare l\\'invio della tua richiesta.";
        statusBanner.style.display = "block";
      }
      window.open(waUrl, "_blank", "noopener,noreferrer");
    } else {
      if (statusBanner) {
        statusBanner.className = "contact-status-banner is-success";
        statusBanner.innerHTML = "<strong>Grazie " + nameVal + "!</strong> La tua richiesta per il servizio <em>\\\"" + serviceVal + "\\\"</em> è stata inviata con successo. Ti risponderemo al più presto!";
        statusBanner.style.display = "block";
      }
      form.reset();
    }
  });
}
"""

with open("js/main.js", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("/**\n * Inizializza il modulo di richiesta preventivo")
clean_text = text[:idx] + code
with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(clean_text)

print("Updated js/main.js via script successfully!")

