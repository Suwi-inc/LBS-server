--
-- PostgreSQL database dump
--

-- Dumped from database version 15.7
-- Dumped by pg_dump version 16.3

-- Started on 2024-05-23 01:14:46

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

--
-- TOC entry 2 (class 3079 OID 16782)
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- TOC entry 3376 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16792)
-- Name: admin; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.admin (
    id integer NOT NULL,
    user_name character varying(50) NOT NULL,
    password character varying(128) NOT NULL
);


--
-- TOC entry 216 (class 1259 OID 16795)
-- Name: admin_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.admin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3377 (class 0 OID 0)
-- Dependencies: 216
-- Name: admin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.admin_id_seq OWNED BY public.admin.id;


--
-- TOC entry 217 (class 1259 OID 16796)
-- Name: device; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.device (
    serial_number character varying(50) NOT NULL,
    device_model character varying(128)
);


--
-- TOC entry 218 (class 1259 OID 16799)
-- Name: gsm_cell; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.gsm_cell (
    id integer NOT NULL,
    country_code integer,
    operator_id integer,
    cell_id integer,
    lac integer,
    signal_strength integer,
    age integer,
    location_id integer
);


--
-- TOC entry 219 (class 1259 OID 16802)
-- Name: gsm_cell_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.gsm_cell_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3378 (class 0 OID 0)
-- Dependencies: 219
-- Name: gsm_cell_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.gsm_cell_id_seq OWNED BY public.gsm_cell.id;


--
-- TOC entry 220 (class 1259 OID 16803)
-- Name: ip; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ip (
    id integer NOT NULL,
    ip_address character varying(50),
    location_id integer
);


--
-- TOC entry 221 (class 1259 OID 16806)
-- Name: ip_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ip_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3379 (class 0 OID 0)
-- Dependencies: 221
-- Name: ip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ip_id_seq OWNED BY public.ip.id;


--
-- TOC entry 222 (class 1259 OID 16807)
-- Name: location; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.location (
    id integer NOT NULL,
    latitude numeric(10,7),
    longitude numeric(10,7),
    location_precision integer,
    location_type character varying(10),
    created_on timestamp without time zone,
    updated_on timestamp without time zone
);


--
-- TOC entry 223 (class 1259 OID 16810)
-- Name: location_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3380 (class 0 OID 0)
-- Dependencies: 223
-- Name: location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.location_id_seq OWNED BY public.location.id;


--
-- TOC entry 224 (class 1259 OID 16811)
-- Name: wifi_network; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wifi_network (
    id integer NOT NULL,
    mac character varying(128),
    signal_strength integer,
    age integer,
    location_id integer
);


--
-- TOC entry 225 (class 1259 OID 16814)
-- Name: wifi_network_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wifi_network_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3381 (class 0 OID 0)
-- Dependencies: 225
-- Name: wifi_network_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wifi_network_id_seq OWNED BY public.wifi_network.id;


--
-- TOC entry 3198 (class 2604 OID 16815)
-- Name: admin id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin ALTER COLUMN id SET DEFAULT nextval('public.admin_id_seq'::regclass);


--
-- TOC entry 3199 (class 2604 OID 16816)
-- Name: gsm_cell id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.gsm_cell ALTER COLUMN id SET DEFAULT nextval('public.gsm_cell_id_seq'::regclass);


--
-- TOC entry 3200 (class 2604 OID 16817)
-- Name: ip id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ip ALTER COLUMN id SET DEFAULT nextval('public.ip_id_seq'::regclass);


--
-- TOC entry 3201 (class 2604 OID 16818)
-- Name: location id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.location ALTER COLUMN id SET DEFAULT nextval('public.location_id_seq'::regclass);


--
-- TOC entry 3202 (class 2604 OID 16819)
-- Name: wifi_network id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wifi_network ALTER COLUMN id SET DEFAULT nextval('public.wifi_network_id_seq'::regclass);


--
-- TOC entry 3360 (class 0 OID 16792)
-- Dependencies: 215
-- Data for Name: admin; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.admin (id, user_name, password) VALUES (1, 'test admin', 'token');
INSERT INTO public.admin (id, user_name, password) VALUES (2, 'admin two', 'password');
INSERT INTO public.admin (id, user_name, password) VALUES (3, 'Admin one', 'password');


--
-- TOC entry 3362 (class 0 OID 16796)
-- Dependencies: 217
-- Data for Name: device; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 3363 (class 0 OID 16799)
-- Dependencies: 218
-- Data for Name: gsm_cell; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (1, 262, 2, 86355, 801, 0, 0, 2);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (2, 262, 2, 1795, 801, 0, 0, 3);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (3, 262, 2, 1794, 801, 0, 0, 4);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (4, 262, 2, 211250, 801, 0, 0, 5);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (5, 262, 2, 86353, 801, 0, 0, 6);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (6, 262, 2, 86357, 801, 0, 0, 7);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (7, 262, 2, 83603, 1107, 0, 0, 8);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (8, 262, 2, 867, 776, 0, 0, 9);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (9, 262, 2, 13971, 1107, 0, 0, 10);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (10, 262, 2, 355, 1107, 0, 0, 11);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (11, 262, 2, 329299, 1107, 0, 0, 12);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (12, 262, 2, 83715, 1107, 0, 0, 13);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (13, 262, 2, 165382, 776, 0, 0, 14);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (14, 262, 2, 213267, 1107, 0, 0, 15);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (15, 262, 2, 165397, 801, 0, 0, 16);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (16, 262, 2, 165665, 776, 0, 0, 17);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (17, 262, 2, 67638, 801, 0, 0, 18);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (18, 262, 2, 165381, 776, 0, 0, 19);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (19, 262, 2, 66385, 776, 0, 0, 20);
INSERT INTO public.gsm_cell (id, country_code, operator_id, cell_id, lac, signal_strength, age, location_id) VALUES (20, 262, 2, 1845, 776, 0, 0, 21);


--
-- TOC entry 3365 (class 0 OID 16803)
-- Dependencies: 220
-- Data for Name: ip; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 3367 (class 0 OID 16807)
-- Dependencies: 222
-- Data for Name: location; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (2, 52.5222020, 13.2855120, 1000, 'UMTS', '2010-08-23 16:19:34', '2011-03-15 05:15:41');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (3, 52.5257140, 13.2769070, 5716, 'GSM', '2010-08-23 16:19:34', '2011-03-15 05:15:41');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (4, 52.5240000, 13.2850640, 6280, 'GSM', '2010-08-23 16:19:34', '2011-03-22 15:16:47');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (5, 52.5217440, 13.2854460, 1000, 'UMTS', '2010-08-23 16:19:34', '2011-03-07 06:02:35');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (6, 52.5215150, 13.2934570, 1000, 'UMTS', '2010-08-23 16:19:34', '2010-12-03 15:47:24');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (7, 52.5327300, 13.2891060, 2400, 'UMTS', '2010-08-23 16:19:34', '2011-02-28 05:39:29');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (8, 52.4975750, 13.3496750, 3102, 'UMTS', '2010-08-24 20:49:49', '2011-03-21 15:33:29');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (9, 52.4973590, 13.3500290, 640, 'GSM', '2010-08-24 20:49:49', '2023-11-27 10:51:05');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (10, 52.4974370, 13.3497430, 1000, 'GSM', '2010-08-24 20:49:49', '2011-03-21 15:33:29');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (11, 52.4973780, 13.3496300, 1000, 'GSM', '2010-08-24 20:49:49', '2011-03-21 15:33:29');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (12, 52.4975190, 13.3492230, 3041, 'UMTS', '2010-08-24 20:49:49', '2011-03-11 19:27:59');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (13, 52.4975720, 13.3490550, 1515, 'UMTS', '2010-08-24 20:49:49', '2011-03-21 15:33:29');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (14, 52.4973690, 13.3497050, 1000, 'UMTS', '2010-08-24 20:49:49', '2011-02-24 14:46:19');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (15, 52.4985470, 13.3484910, 2968, 'UMTS', '2010-08-24 20:49:49', '2011-03-18 15:38:03');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (16, 52.4976050, 13.3493110, 1000, 'UMTS', '2010-08-24 20:49:49', '2011-03-21 15:33:29');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (17, 52.4973460, 13.3498940, 1000, 'UMTS', '2010-08-24 20:49:49', '2011-03-21 15:33:29');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (18, 52.4976320, 13.3489020, 1994, 'UMTS', '2010-08-24 20:49:49', '2011-03-21 15:33:29');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (19, 52.4975140, 13.3488570, 1503, 'UMTS', '2010-08-24 20:49:49', '2011-03-21 15:21:12');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (20, 52.4986680, 13.3478630, 2933, 'UMTS', '2010-08-24 20:49:49', '2011-03-21 15:21:12');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (21, 52.4973990, 13.3495440, 1000, 'GSM', '2010-08-24 20:49:49', '2011-03-21 15:33:29');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (23, 45.2212839, 16.5483825, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (24, 45.2202797, 16.5470705, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (25, 45.2082862, 16.9038547, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (26, 45.2079946, 16.9033616, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (27, 45.1757026, 16.8172025, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (28, 45.1873223, 16.8343192, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (29, 45.1805467, 16.8105353, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (30, 45.1819114, 16.8094643, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (31, 45.2079148, 16.9027264, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (32, 45.1923268, 16.8443886, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (33, 45.1862184, 16.8306459, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (34, 45.1745276, 16.8122005, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (35, 45.2076476, 16.8999650, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (36, 45.1754706, 16.8108573, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (37, 45.1911525, 16.8430917, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (38, 45.1758905, 16.8107214, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (39, 45.1746108, 16.8128450, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (40, 45.1793499, 16.8227714, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (41, 45.1761872, 16.8183730, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');
INSERT INTO public.location (id, latitude, longitude, location_precision, location_type, created_on, updated_on) VALUES (42, 45.1813743, 16.8099072, 0, 'WIFI', '1970-01-01 00:00:00', '2015-04-08 20:19:15');


--
-- TOC entry 3369 (class 0 OID 16811)
-- Dependencies: 224
-- Data for Name: wifi_network; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (1, '0001E3C290F9', 0, 0, 23);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (2, '000C421F65E9', 0, 0, 24);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (3, '000C422377FC', 0, 0, 25);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (4, '000C422377F4', 0, 0, 26);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (5, '000C422377C5', 0, 0, 27);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (6, '000C42630AED', 0, 0, 28);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (7, '000C42630AEC', 0, 0, 29);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (8, '0005595C556A', 0, 0, 30);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (9, '000C421BB4FE', 0, 0, 31);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (10, '000C422CC930', 0, 0, 32);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (11, '0005595C7B59', 0, 0, 33);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (12, '000C420CCF25', 0, 0, 34);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (13, '000559604EC0', 0, 0, 35);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (14, '000C42654000', 0, 0, 36);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (15, '00040EDA3168', 0, 0, 37);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (16, '000559602166', 0, 0, 38);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (17, '000FFD1F37D8', 0, 0, 39);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (18, '000C4223D3BF', 0, 0, 40);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (19, '000C42059D59', 0, 0, 41);
INSERT INTO public.wifi_network (id, mac, signal_strength, age, location_id) VALUES (20, '000C420C4B40', 0, 0, 42);


--
-- TOC entry 3382 (class 0 OID 0)
-- Dependencies: 216
-- Name: admin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.admin_id_seq', 1, false);


--
-- TOC entry 3383 (class 0 OID 0)
-- Dependencies: 219
-- Name: gsm_cell_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.gsm_cell_id_seq', 1, false);


--
-- TOC entry 3384 (class 0 OID 0)
-- Dependencies: 221
-- Name: ip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ip_id_seq', 1, false);


--
-- TOC entry 3385 (class 0 OID 0)
-- Dependencies: 223
-- Name: location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.location_id_seq', 1, false);


--
-- TOC entry 3386 (class 0 OID 0)
-- Dependencies: 225
-- Name: wifi_network_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wifi_network_id_seq', 1, false);


--
-- TOC entry 3204 (class 2606 OID 16821)
-- Name: admin admin_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id);


--
-- TOC entry 3206 (class 2606 OID 16823)
-- Name: device device_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_pkey PRIMARY KEY (serial_number);


--
-- TOC entry 3208 (class 2606 OID 16825)
-- Name: gsm_cell gsm_cell_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.gsm_cell
    ADD CONSTRAINT gsm_cell_pkey PRIMARY KEY (id);


--
-- TOC entry 3210 (class 2606 OID 16827)
-- Name: ip ip_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ip
    ADD CONSTRAINT ip_pkey PRIMARY KEY (id);


--
-- TOC entry 3212 (class 2606 OID 16829)
-- Name: location location_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (id);


--
-- TOC entry 3214 (class 2606 OID 16831)
-- Name: wifi_network wifi_network_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wifi_network
    ADD CONSTRAINT wifi_network_pkey PRIMARY KEY (id);


--
-- TOC entry 3215 (class 2606 OID 16832)
-- Name: gsm_cell gsm_cell_location_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.gsm_cell
    ADD CONSTRAINT gsm_cell_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.location(id) ON DELETE CASCADE;


--
-- TOC entry 3216 (class 2606 OID 16837)
-- Name: ip ip_location_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ip
    ADD CONSTRAINT ip_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.location(id) ON DELETE CASCADE;


--
-- TOC entry 3217 (class 2606 OID 16842)
-- Name: wifi_network wifi_network_location_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wifi_network
    ADD CONSTRAINT wifi_network_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.location(id) ON DELETE CASCADE;


-- Completed on 2024-05-23 01:14:46

--
-- PostgreSQL database dump complete
--

