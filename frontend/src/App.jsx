import { useEffect, useRef, useState } from 'react';
import './App.css';
import profileImage from './assets/profile-photo.png';
import {
  certificates,
  navLinks,
  profile,
  projects as fallbackProjects,
  skillGroups,
} from './data';

const apiBaseUrl = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

function App() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');
  const [menuOpen, setMenuOpen] = useState(false);
  const [profilePhoto, setProfilePhoto] = useState(() => {
    try {
      const savedPhoto = localStorage.getItem('portfolio-profile-photo');
      return savedPhoto?.startsWith('data:image/') ? savedPhoto : profileImage;
    } catch {
      return profileImage;
    }
  });
  const fileInputRef = useRef(null);

  useEffect(() => {
    let isMounted = true;

    const loadProjects = async () => {
      try {
        const response = await fetch(`${apiBaseUrl}/api/projects/`);
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }

        const payload = await response.json();

        if (!isMounted) {
          return;
        }

        setProjects(payload.projects || []);
        setLoading(false);
      } catch (error) {
        if (!isMounted) {
          return;
        }

        setProjects(fallbackProjects);
        setErrorMessage(
          'The Django API is not available right now, so the portfolio is showing local fallback project data.',
        );
        setLoading(false);
      }
    };

    loadProjects();

    return () => {
      isMounted = false;
    };
  }, []);

  useEffect(() => {
    try {
      localStorage.setItem('portfolio-profile-photo', profilePhoto);
    } catch {
      // ignore storage errors in restricted browser contexts
    }
  }, [profilePhoto]);

  const handleImageSelect = (event) => {
    const file = event.target.files?.[0];
    if (!file) {
      return;
    }

    if (!file.type.startsWith('image/')) {
      event.target.value = '';
      return;
    }

    const reader = new FileReader();
    reader.onload = (loadEvent) => {
      setProfilePhoto(loadEvent.target?.result || profileImage);
    };
    reader.readAsDataURL(file);
    event.target.value = '';
  };

  const handleRemovePhoto = () => {
    setProfilePhoto(profileImage);
    try {
      localStorage.removeItem('portfolio-profile-photo');
    } catch {
      // ignore storage errors in restricted browser contexts
    }
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleProfileKeyDown = (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      fileInputRef.current?.click();
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    window.alert(
      'This demo form is ready to be connected to a backend email service or SMTP provider.',
    );
  };

  return (
    <div className="page-shell">
      <header className="site-header">
        <div className="container nav-container">
          <a className="brand" href="#home" aria-label="Go to home section">
            {profile.name}
          </a>

          <button
            className="menu-toggle"
            type="button"
            aria-expanded={menuOpen}
            aria-controls="nav-menu"
            aria-label="Toggle menu"
            onClick={() => setMenuOpen((prev) => !prev)}
          >
            {menuOpen ? 'Close' : 'Menu'}
          </button>

          <nav id="nav-menu" className={`main-nav ${menuOpen ? 'open' : ''}`}>
            {navLinks.map((link) => (
              <a key={link.href} href={link.href} onClick={() => setMenuOpen(false)}>
                {link.label}
              </a>
            ))}
          </nav>
        </div>
      </header>

      <main>
        <section id="home" className="hero-section">
          <div className="container hero-layout">
            <div className="hero-copy">
              <p className="eyebrow">Recent graduate • Computer Science</p>
              <h1>
                Hi, I&apos;m <span>{profile.name}</span>
              </h1>
              <h2>{profile.title}</h2>
              <p className="lead">{profile.intro}</p>

              <div className="cta-row">
                <a className="primary-button" href="#projects">
                  View My Projects
                </a>
                <a
                  className="primary-button github-button"
                  href={profile.githubUrl}
                  target="_blank"
                  rel="noreferrer"
                >
                  GitHub Profile
                </a>
                <a className="secondary-button" href="#contact">
                  Contact Me
                </a>
              </div>

              <div className="social-row" aria-label="Social links">
                <a href={profile.githubUrl} target="_blank" rel="noreferrer">
                  GitHub
                </a>
                <a href={profile.linkedinUrl} target="_blank" rel="noreferrer">
                  LinkedIn
                </a>
              </div>
            </div>

            <div className="hero-panel" aria-label="Profile overview card">
              <div className="panel-glow" aria-hidden="true" />
              <div
                className="profile-visual"
                onClick={() => fileInputRef.current?.click()}
                onKeyDown={handleProfileKeyDown}
                role="button"
                tabIndex={0}
                aria-label="Upload or change profile photo"
              >
                <img
                  src={profilePhoto}
                  alt="Abebe Gashe profile portrait"
                  className="profile-photo"
                />
                <div className="profile-overlay">
                  <span className="profile-edit-badge">Edit</span>
                </div>
                {profilePhoto !== profileImage && (
                  <button
                    type="button"
                    className="remove-photo-button"
                    onClick={(event) => {
                      event.stopPropagation();
                      handleRemovePhoto();
                    }}
                    aria-label="Remove profile photo"
                  >
                    Remove
                  </button>
                )}
                <input
                  ref={fileInputRef}
                  type="file"
                  accept="image/*"
                  className="hidden-file-input"
                  onChange={handleImageSelect}
                />
              </div>
              <div className="mini-card">
                <span className="tag">Core stack</span>
                <div className="stack-pills">
                  <span>Python</span>
                  <span>Django</span>
                  <span>React</span>
                  <span>SQLite</span>
                </div>
              </div>

              <div className="mini-card detail-card">
                <span className="tag">Focus areas</span>
                <ul>
                  <li>Backend web development</li>
                  <li>Database systems</li>
                  <li>AI-assisted applications</li>
                  <li>Practical software solutions</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <section id="about" className="content-section">
          <div className="container section-inner">
            <div className="section-header">
              <p className="eyebrow">About Me</p>
              <h3>Developer with a strong foundation in practical software engineering.</h3>
            </div>

            <div className="about-grid">
              <div className="about-copy">
                <p>
                  I am a recent graduate in Computer Science from the University of Gondar,
                  currently exploring software development through practical projects, backend
                  engineering, and full-stack application design. I am especially interested in
                  building useful software solutions, working with databases, and creating
                  user-focused web applications.
                </p>
                <p>
                  My interests include backend development, full-stack web development,
                  database systems, and AI-assisted applications, with an emphasis on writing
                  robust and maintainable code.
                </p>
              </div>

              <div className="education-card">
                <h4>Education</h4>
                <ul>
                  <li>
                    <strong>BSc in Computer Science</strong>
                  </li>
                  <li>University of Gondar</li>
                  <li>2022–2026</li>
                  <li>CGPA: 3.62</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <section id="skills" className="content-section alt-section">
          <div className="container">
            <div className="section-header centered">
              <p className="eyebrow">Skills</p>
              <h3>Technologies and tools I am building with.</h3>
            </div>

            <div className="skills-grid">
              {skillGroups.map((group) => (
                <article className="skill-card" key={group.title}>
                  <h4>{group.title}</h4>
                  <ul>
                    {group.items.map((skill) => (
                      <li key={skill}>{skill}</li>
                    ))}
                  </ul>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section id="projects" className="content-section">
          <div className="container">
            <div className="section-header centered">
              <p className="eyebrow">Projects</p>
              <h3>Featured work and project experience.</h3>
            </div>

            {loading && <p className="status-message">Loading project data...</p>}

            {!loading && errorMessage && (
              <p className="status-message warning">{errorMessage}</p>
            )}

            <div className="projects-grid">
              {projects.map((project) => (
                <article className="project-card" key={project.id || project.name}>
                  <div className="project-meta">
                    <span className="project-status">{project.status || 'Featured project'}</span>
                  </div>
                  <h4>{project.name}</h4>
                  <p>{project.description}</p>

                  <div className="tech-stack">
                    {project.technologies.map((tech) => (
                      <span key={`${project.id}-${tech}`}>{tech}</span>
                    ))}
                  </div>

                  <div className="project-links">
                    <a
                      className="primary-button"
                      href={project.github}
                      target="_blank"
                      rel="noreferrer"
                    >
                      GitHub Link
                    </a>
                    <a
                      className="primary-button"
                      href={project.live_demo}
                      target="_blank"
                      rel="noreferrer"
                    >
                      View Project
                    </a>
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section id="certifications" className="content-section alt-section">
          <div className="container">
            <div className="section-header centered">
              <p className="eyebrow">Certifications</p>
              <h3>Learning milestones and completed courses.</h3>
            </div>

            <div className="certificates-grid">
              {certificates.map((certificate) => (
                <article className="certificate-card" key={certificate.name}>
                  <div className="certificate-icon" aria-hidden="true">
                    ✓
                  </div>
                  <h4>{certificate.name}</h4>
                  <p>{certificate.provider}</p>
                  <p className="certificate-date">{certificate.issueDate}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section id="contact" className="content-section">
          <div className="container contact-layout">
            <div>
              <div className="section-header">
                <p className="eyebrow">Contact</p>
                <h3>Let&apos;s build something useful.</h3>
              </div>

              <div className="contact-list">
                <a href={`mailto:${profile.email}`}>{profile.email}</a>
                <a href={profile.portfolioUrl} target="_blank" rel="noreferrer">
                  Portfolio
                </a>
                <a href={profile.githubUrl} target="_blank" rel="noreferrer">
                  GitHub
                </a>
                <a href={profile.linkedinUrl} target="_blank" rel="noreferrer">
                  LinkedIn
                </a>
              </div>
            </div>

            <form className="contact-form" onSubmit={handleSubmit}>
              <label>
                Name
                <input type="text" name="name" placeholder="Your name" />
              </label>
              <label>
                Email
                <input type="email" name="email" placeholder="you@example.com" />
              </label>
              <label>
                Message
                <textarea name="message" placeholder="Tell me about your project" rows="4" />
              </label>
              <button type="submit">Send Message</button>
            </form>
          </div>
        </section>
      </main>

      <footer className="site-footer">
        <div className="container footer-layout">
          <p>© <span>{new Date().getFullYear()}</span> {profile.name}</p>
          <div className="footer-links">
            {navLinks.map((link) => (
              <a key={link.href} href={link.href}>
                {link.label}
              </a>
            ))}
            <a href={profile.githubUrl} target="_blank" rel="noreferrer">
              GitHub
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
