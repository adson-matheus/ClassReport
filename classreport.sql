--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: aula_aula; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aula_aula (
    id bigint NOT NULL,
    assunto character varying(255),
    datetime timestamp with time zone NOT NULL,
    turma_id bigint
);


ALTER TABLE public.aula_aula OWNER TO postgres;

--
-- Name: aula_aula_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aula_aula_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aula_aula_id_seq OWNER TO postgres;

--
-- Name: aula_aula_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aula_aula_id_seq OWNED BY public.aula_aula.id;


--
-- Name: aula_auladoaluno; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aula_auladoaluno (
    id bigint NOT NULL,
    presenca boolean,
    aluno_id bigint NOT NULL,
    aula_id bigint NOT NULL
);


ALTER TABLE public.aula_auladoaluno OWNER TO postgres;

--
-- Name: aula_auladoaluno_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aula_auladoaluno_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aula_auladoaluno_id_seq OWNER TO postgres;

--
-- Name: aula_auladoaluno_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aula_auladoaluno_id_seq OWNED BY public.aula_auladoaluno.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: avaliacao_avaliacao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.avaliacao_avaliacao (
    id bigint NOT NULL,
    checklist jsonb NOT NULL,
    aula_do_aluno_id bigint NOT NULL
);


ALTER TABLE public.avaliacao_avaliacao OWNER TO postgres;

--
-- Name: avaliacao_avaliacao_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.avaliacao_avaliacao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.avaliacao_avaliacao_id_seq OWNER TO postgres;

--
-- Name: avaliacao_avaliacao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.avaliacao_avaliacao_id_seq OWNED BY public.avaliacao_avaliacao.id;


--
-- Name: avaliacao_avaliacoesprofessor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.avaliacao_avaliacoesprofessor (
    id bigint NOT NULL,
    id_avaliacao_id bigint,
    id_professor_id character varying(20)
);


ALTER TABLE public.avaliacao_avaliacoesprofessor OWNER TO postgres;

--
-- Name: avaliacao_avaliacoesprofessor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.avaliacao_avaliacoesprofessor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.avaliacao_avaliacoesprofessor_id_seq OWNER TO postgres;

--
-- Name: avaliacao_avaliacoesprofessor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.avaliacao_avaliacoesprofessor_id_seq OWNED BY public.avaliacao_avaliacoesprofessor.id;


--
-- Name: disciplina_disciplina; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.disciplina_disciplina (
    id bigint NOT NULL,
    nome character varying(255)
);


ALTER TABLE public.disciplina_disciplina OWNER TO postgres;

--
-- Name: disciplina_disciplina_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.disciplina_disciplina_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.disciplina_disciplina_id_seq OWNER TO postgres;

--
-- Name: disciplina_disciplina_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.disciplina_disciplina_id_seq OWNED BY public.disciplina_disciplina.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: turma_turma; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.turma_turma (
    id bigint NOT NULL,
    ano integer,
    periodo integer,
    descricao character varying(255),
    disciplina_id bigint NOT NULL,
    professor_id character varying(20) NOT NULL
);


ALTER TABLE public.turma_turma OWNER TO postgres;

--
-- Name: turma_turma_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.turma_turma_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.turma_turma_id_seq OWNER TO postgres;

--
-- Name: turma_turma_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.turma_turma_id_seq OWNED BY public.turma_turma.id;


--
-- Name: users_administrador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_administrador (
    siape character varying(20) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.users_administrador OWNER TO postgres;

--
-- Name: users_aluno; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_aluno (
    id bigint NOT NULL,
    matricula character varying(20) NOT NULL,
    nome character varying(100) NOT NULL
);


ALTER TABLE public.users_aluno OWNER TO postgres;

--
-- Name: users_aluno_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_aluno_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_aluno_id_seq OWNER TO postgres;

--
-- Name: users_aluno_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_aluno_id_seq OWNED BY public.users_aluno.id;


--
-- Name: users_professor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users_professor (
    siape character varying(20) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.users_professor OWNER TO postgres;

--
-- Name: aula_aula id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aula_aula ALTER COLUMN id SET DEFAULT nextval('public.aula_aula_id_seq'::regclass);


--
-- Name: aula_auladoaluno id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aula_auladoaluno ALTER COLUMN id SET DEFAULT nextval('public.aula_auladoaluno_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: avaliacao_avaliacao id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao_avaliacao ALTER COLUMN id SET DEFAULT nextval('public.avaliacao_avaliacao_id_seq'::regclass);


--
-- Name: avaliacao_avaliacoesprofessor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao_avaliacoesprofessor ALTER COLUMN id SET DEFAULT nextval('public.avaliacao_avaliacoesprofessor_id_seq'::regclass);


--
-- Name: disciplina_disciplina id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disciplina_disciplina ALTER COLUMN id SET DEFAULT nextval('public.disciplina_disciplina_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: turma_turma id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.turma_turma ALTER COLUMN id SET DEFAULT nextval('public.turma_turma_id_seq'::regclass);


--
-- Name: users_aluno id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_aluno ALTER COLUMN id SET DEFAULT nextval('public.users_aluno_id_seq'::regclass);


--
-- Data for Name: aula_aula; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.aula_aula (id, assunto, datetime, turma_id) FROM stdin;
\.


--
-- Data for Name: aula_auladoaluno; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.aula_auladoaluno (id, presenca, aluno_id, aula_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
1	grp_administradores
2	grp_professores
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	25
2	1	26
3	1	27
4	1	28
5	1	29
6	1	30
7	1	31
8	1	32
9	1	33
10	1	34
11	1	35
12	1	36
13	1	40
14	1	44
15	1	45
16	1	46
17	1	47
18	1	48
19	1	49
20	1	50
21	1	51
22	1	52
23	1	53
24	1	54
25	1	55
26	1	56
27	1	57
28	1	58
29	1	59
30	1	60
31	2	34
32	2	35
33	2	36
34	2	37
35	2	38
36	2	39
37	2	40
38	2	41
39	2	42
40	2	43
41	2	44
42	2	48
43	2	56
44	2	28
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add aluno	7	add_aluno
26	Can change aluno	7	change_aluno
27	Can delete aluno	7	delete_aluno
28	Can view aluno	7	view_aluno
29	Can add administrador	8	add_administrador
30	Can change administrador	8	change_administrador
31	Can delete administrador	8	delete_administrador
32	Can view administrador	8	view_administrador
33	Can add professor	9	add_professor
34	Can change professor	9	change_professor
35	Can delete professor	9	delete_professor
36	Can view professor	9	view_professor
37	Can add avaliacao	10	add_avaliacao
38	Can change avaliacao	10	change_avaliacao
39	Can delete avaliacao	10	delete_avaliacao
40	Can view avaliacao	10	view_avaliacao
41	Can add avaliacoes professor	11	add_avaliacoesprofessor
42	Can change avaliacoes professor	11	change_avaliacoesprofessor
43	Can delete avaliacoes professor	11	delete_avaliacoesprofessor
44	Can view avaliacoes professor	11	view_avaliacoesprofessor
45	Can add aula	12	add_aula
46	Can change aula	12	change_aula
47	Can delete aula	12	delete_aula
48	Can view aula	12	view_aula
49	Can add aula do aluno	13	add_auladoaluno
50	Can change aula do aluno	13	change_auladoaluno
51	Can delete aula do aluno	13	delete_auladoaluno
52	Can view aula do aluno	13	view_auladoaluno
53	Can add disciplina	14	add_disciplina
54	Can change disciplina	14	change_disciplina
55	Can delete disciplina	14	delete_disciplina
56	Can view disciplina	14	view_disciplina
57	Can add turma	15	add_turma
58	Can change turma	15	change_turma
59	Can delete turma	15	delete_turma
60	Can view turma	15	view_turma
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$320000$jJnobP3VtWjSaybOVCRR1M$x7PxnK3+Le+g89naRl/nAiwhbWqDD3prFg7/Aa/YXvQ=	2022-08-26 09:42:19.862381-03	t	ufrn				t	t	2022-08-25 14:14:45-03
3	pbkdf2_sha256$320000$zUoelIh1xaocOTjq2kQJTa$kQr0t2E0/QxPtN2FFCWPYw1BI4Wi3Wx3J/zMGMMvKTQ=	2022-08-26 13:13:54.34015-03	f	taciano	Taciano	Silva	taciano@mail.com	f	t	2022-08-26 10:17:44.438742-03
2	pbkdf2_sha256$320000$exeqY0ld6XNwojUWqBJOqK$kIRllNhK22fGQ4HZjmMQaDKyrujoZb4mIKG4TqciTjc=	2022-08-26 13:23:00.915824-03	f	marinna	Marinna	Maria	marinna@mail.com	f	t	2022-08-25 14:36:28.591266-03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
1	1	1
2	2	1
3	3	2
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: avaliacao_avaliacao; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.avaliacao_avaliacao (id, checklist, aula_do_aluno_id) FROM stdin;
\.


--
-- Data for Name: avaliacao_avaliacoesprofessor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.avaliacao_avaliacoesprofessor (id, id_avaliacao_id, id_professor_id) FROM stdin;
\.


--
-- Data for Name: disciplina_disciplina; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.disciplina_disciplina (id, nome) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-08-25 14:29:36.264732-03	1	grp_administradores	1	[{"added": {}}]	3	1
2	2022-08-25 14:30:28.824889-03	2	grp_professores	1	[{"added": {}}]	3	1
3	2022-08-25 14:32:12.818306-03	1	ufrn	2	[{"changed": {"fields": ["Groups"]}}]	4	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	users	aluno
8	users	administrador
9	users	professor
10	avaliacao	avaliacao
11	avaliacao	avaliacoesprofessor
12	aula	aula
13	aula	auladoaluno
14	disciplina	disciplina
15	turma	turma
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-08-25 14:14:26.67004-03
2	auth	0001_initial	2022-08-25 14:14:26.75921-03
3	admin	0001_initial	2022-08-25 14:14:26.784466-03
4	admin	0002_logentry_remove_auto_add	2022-08-25 14:14:26.796355-03
5	admin	0003_logentry_add_action_flag_choices	2022-08-25 14:14:26.805957-03
6	users	0001_initial	2022-08-25 14:14:26.821896-03
7	users	0002_administrador	2022-08-25 14:14:26.860519-03
8	users	0003_alter_administrador_options_professor	2022-08-25 14:14:26.892842-03
9	disciplina	0001_initial	2022-08-25 14:14:26.901227-03
10	turma	0001_initial	2022-08-25 14:14:26.930244-03
11	aula	0001_initial	2022-08-25 14:14:26.950138-03
12	aula	0002_auladoaluno	2022-08-25 14:14:26.974137-03
13	contenttypes	0002_remove_content_type_name	2022-08-25 14:14:26.997736-03
14	auth	0002_alter_permission_name_max_length	2022-08-25 14:14:27.012784-03
15	auth	0003_alter_user_email_max_length	2022-08-25 14:14:27.022605-03
16	auth	0004_alter_user_username_opts	2022-08-25 14:14:27.033132-03
17	auth	0005_alter_user_last_login_null	2022-08-25 14:14:27.044137-03
18	auth	0006_require_contenttypes_0002	2022-08-25 14:14:27.047075-03
19	auth	0007_alter_validators_add_error_messages	2022-08-25 14:14:27.05682-03
20	auth	0008_alter_user_username_max_length	2022-08-25 14:14:27.072293-03
21	auth	0009_alter_user_last_name_max_length	2022-08-25 14:14:27.084187-03
22	auth	0010_alter_group_name_max_length	2022-08-25 14:14:27.112444-03
23	auth	0011_update_proxy_permissions	2022-08-25 14:14:27.126206-03
24	auth	0012_alter_user_first_name_max_length	2022-08-25 14:14:27.137644-03
25	avaliacao	0001_initial	2022-08-25 14:14:27.190708-03
26	sessions	0001_initial	2022-08-25 14:14:27.206841-03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
ghp5lstkc0as489ys2mr2emobypgvabu	.eJxVjDsOwjAQBe_iGlm24x-U9DmDtV7v4gBypDipEHeHSCmgfTPzXiLBtta0dVrSVMRFGHH63TLgg9oOyh3abZY4t3WZstwVedAux7nQ83q4fwcVev3Wzg_MqMipoMkwZCI7oEKOxvri2TttzjYCcrYcFWsDRlkbXCghc0Dx_gD01jgz:1oRHtf:_OY32belqdmwSoE4SmwklwN1-4iFN5CHdWT8Awozu3k	2022-09-08 15:48:07.897815-03
urdx1b9l2j19lrl2xi9xgcqbi4qij1xo	.eJxVTEsKwyAUvIvrIv41XXafM4hPnzVtUYjJqvTuNZBFCzMMzO9NfNi34veOq18SuRJOLr8ehPjEegTpEeq90djqti5Ajwo9007nlvB1O7t_ByX0MtZWOCO5ZTxmnJhQcSgaJTWGbAMDxjlM0jhtVQYQOg7KNKCky04I8vkC07w3ag:1oRX2N:IrCB00ABeunC4UvP-AGGK98PmqvUtvj-0O_JUgOaAtQ	2022-09-09 07:58:07.965988-03
\.


--
-- Data for Name: turma_turma; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.turma_turma (id, ano, periodo, descricao, disciplina_id, professor_id) FROM stdin;
\.


--
-- Data for Name: users_administrador; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_administrador (siape, user_id) FROM stdin;
3091078	2
\.


--
-- Data for Name: users_aluno; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_aluno (id, matricula, nome) FROM stdin;
\.


--
-- Data for Name: users_professor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users_professor (siape, user_id) FROM stdin;
12345	3
\.


--
-- Name: aula_aula_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.aula_aula_id_seq', 1, false);


--
-- Name: aula_auladoaluno_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.aula_auladoaluno_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 44, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 60, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 3, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 3, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: avaliacao_avaliacao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.avaliacao_avaliacao_id_seq', 1, false);


--
-- Name: avaliacao_avaliacoesprofessor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.avaliacao_avaliacoesprofessor_id_seq', 1, false);


--
-- Name: disciplina_disciplina_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.disciplina_disciplina_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 3, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- Name: turma_turma_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.turma_turma_id_seq', 1, false);


--
-- Name: users_aluno_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_aluno_id_seq', 1, false);


--
-- Name: aula_aula aula_aula_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aula_aula
    ADD CONSTRAINT aula_aula_pkey PRIMARY KEY (id);


--
-- Name: aula_auladoaluno aula_auladoaluno_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aula_auladoaluno
    ADD CONSTRAINT aula_auladoaluno_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: avaliacao_avaliacao avaliacao_avaliacao_aula_do_aluno_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao_avaliacao
    ADD CONSTRAINT avaliacao_avaliacao_aula_do_aluno_id_key UNIQUE (aula_do_aluno_id);


--
-- Name: avaliacao_avaliacao avaliacao_avaliacao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao_avaliacao
    ADD CONSTRAINT avaliacao_avaliacao_pkey PRIMARY KEY (id);


--
-- Name: avaliacao_avaliacoesprofessor avaliacao_avaliacoesprofessor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao_avaliacoesprofessor
    ADD CONSTRAINT avaliacao_avaliacoesprofessor_pkey PRIMARY KEY (id);


--
-- Name: disciplina_disciplina disciplina_disciplina_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disciplina_disciplina
    ADD CONSTRAINT disciplina_disciplina_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: turma_turma turma_turma_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.turma_turma
    ADD CONSTRAINT turma_turma_pkey PRIMARY KEY (id);


--
-- Name: users_administrador users_administrador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_administrador
    ADD CONSTRAINT users_administrador_pkey PRIMARY KEY (siape);


--
-- Name: users_administrador users_administrador_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_administrador
    ADD CONSTRAINT users_administrador_user_id_key UNIQUE (user_id);


--
-- Name: users_aluno users_aluno_matricula_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_aluno
    ADD CONSTRAINT users_aluno_matricula_key UNIQUE (matricula);


--
-- Name: users_aluno users_aluno_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_aluno
    ADD CONSTRAINT users_aluno_pkey PRIMARY KEY (id);


--
-- Name: users_professor users_professor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_professor
    ADD CONSTRAINT users_professor_pkey PRIMARY KEY (siape);


--
-- Name: users_professor users_professor_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_professor
    ADD CONSTRAINT users_professor_user_id_key UNIQUE (user_id);


--
-- Name: aula_aula_turma_id_3c5b80b4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX aula_aula_turma_id_3c5b80b4 ON public.aula_aula USING btree (turma_id);


--
-- Name: aula_auladoaluno_aluno_id_123ef3d7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX aula_auladoaluno_aluno_id_123ef3d7 ON public.aula_auladoaluno USING btree (aluno_id);


--
-- Name: aula_auladoaluno_aula_id_87f922dc; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX aula_auladoaluno_aula_id_87f922dc ON public.aula_auladoaluno USING btree (aula_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: avaliacao_avaliacoesprofessor_id_avaliacao_id_93efb59c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX avaliacao_avaliacoesprofessor_id_avaliacao_id_93efb59c ON public.avaliacao_avaliacoesprofessor USING btree (id_avaliacao_id);


--
-- Name: avaliacao_avaliacoesprofessor_id_professor_id_176693d4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX avaliacao_avaliacoesprofessor_id_professor_id_176693d4 ON public.avaliacao_avaliacoesprofessor USING btree (id_professor_id);


--
-- Name: avaliacao_avaliacoesprofessor_id_professor_id_176693d4_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX avaliacao_avaliacoesprofessor_id_professor_id_176693d4_like ON public.avaliacao_avaliacoesprofessor USING btree (id_professor_id varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: turma_turma_disciplina_id_d4f57f09; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX turma_turma_disciplina_id_d4f57f09 ON public.turma_turma USING btree (disciplina_id);


--
-- Name: turma_turma_professor_id_33407bdd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX turma_turma_professor_id_33407bdd ON public.turma_turma USING btree (professor_id);


--
-- Name: turma_turma_professor_id_33407bdd_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX turma_turma_professor_id_33407bdd_like ON public.turma_turma USING btree (professor_id varchar_pattern_ops);


--
-- Name: users_administrador_siape_0243eff1_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_administrador_siape_0243eff1_like ON public.users_administrador USING btree (siape varchar_pattern_ops);


--
-- Name: users_aluno_matricula_91996395_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_aluno_matricula_91996395_like ON public.users_aluno USING btree (matricula varchar_pattern_ops);


--
-- Name: users_professor_siape_b6a7d2da_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX users_professor_siape_b6a7d2da_like ON public.users_professor USING btree (siape varchar_pattern_ops);


--
-- Name: aula_aula aula_aula_turma_id_3c5b80b4_fk_turma_turma_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aula_aula
    ADD CONSTRAINT aula_aula_turma_id_3c5b80b4_fk_turma_turma_id FOREIGN KEY (turma_id) REFERENCES public.turma_turma(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: aula_auladoaluno aula_auladoaluno_aluno_id_123ef3d7_fk_users_aluno_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aula_auladoaluno
    ADD CONSTRAINT aula_auladoaluno_aluno_id_123ef3d7_fk_users_aluno_id FOREIGN KEY (aluno_id) REFERENCES public.users_aluno(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: aula_auladoaluno aula_auladoaluno_aula_id_87f922dc_fk_aula_aula_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aula_auladoaluno
    ADD CONSTRAINT aula_auladoaluno_aula_id_87f922dc_fk_aula_aula_id FOREIGN KEY (aula_id) REFERENCES public.aula_aula(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: avaliacao_avaliacao avaliacao_avaliacao_aula_do_aluno_id_b2130de6_fk_aula_aula; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao_avaliacao
    ADD CONSTRAINT avaliacao_avaliacao_aula_do_aluno_id_b2130de6_fk_aula_aula FOREIGN KEY (aula_do_aluno_id) REFERENCES public.aula_auladoaluno(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: avaliacao_avaliacoesprofessor avaliacao_avaliacoes_id_avaliacao_id_93efb59c_fk_avaliacao; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao_avaliacoesprofessor
    ADD CONSTRAINT avaliacao_avaliacoes_id_avaliacao_id_93efb59c_fk_avaliacao FOREIGN KEY (id_avaliacao_id) REFERENCES public.avaliacao_avaliacao(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: avaliacao_avaliacoesprofessor avaliacao_avaliacoes_id_professor_id_176693d4_fk_users_pro; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.avaliacao_avaliacoesprofessor
    ADD CONSTRAINT avaliacao_avaliacoes_id_professor_id_176693d4_fk_users_pro FOREIGN KEY (id_professor_id) REFERENCES public.users_professor(siape) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: turma_turma turma_turma_disciplina_id_d4f57f09_fk_disciplina_disciplina_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.turma_turma
    ADD CONSTRAINT turma_turma_disciplina_id_d4f57f09_fk_disciplina_disciplina_id FOREIGN KEY (disciplina_id) REFERENCES public.disciplina_disciplina(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: turma_turma turma_turma_professor_id_33407bdd_fk_users_professor_siape; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.turma_turma
    ADD CONSTRAINT turma_turma_professor_id_33407bdd_fk_users_professor_siape FOREIGN KEY (professor_id) REFERENCES public.users_professor(siape) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_administrador users_administrador_user_id_45b29c77_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_administrador
    ADD CONSTRAINT users_administrador_user_id_45b29c77_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_professor users_professor_user_id_fb0dbe59_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users_professor
    ADD CONSTRAINT users_professor_user_id_fb0dbe59_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

