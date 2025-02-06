


CREATE TABLE public.customers (
	customer_id bigserial NOT NULL,
	"name" varchar(100) NOT NULL,
	phone varchar(10) NOT NULL,
	address varchar(100) NOT NULL,
	CONSTRAINT customers_pkey PRIMARY KEY (customer_id)
);

CREATE TABLE public.drivers (
	driver_id bigserial NOT NULL,
	"name" varchar(100) NOT NULL,
	phone varchar(10) NOT NULL,
	car_number varchar(15) NOT NULL,
	availability int4 DEFAULT 1 NULL,
	CONSTRAINT drivers_pkey PRIMARY KEY (driver_id)
);

CREATE TABLE public.orders (
	order_id bigserial NOT NULL,
	customer_id int4 NULL,
	amount numeric(10, 2) NOT NULL,
	status varchar(50) DEFAULT 'pending'::character varying NULL,
	CONSTRAINT orders_pkey PRIMARY KEY (order_id),
	CONSTRAINT orders_status_check CHECK (((status)::text = ANY ((ARRAY['pending'::character varying, 'paid'::character varying, 'out for delivery'::character varying, 'delivered'::character varying])::text[])))
);


-- public.orders foreign keys

ALTER TABLE public.orders ADD CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


CREATE TABLE public.rides (
	ride_id bigserial NOT NULL,
	customer_id int4 NULL,
	amount numeric(10, 2) NOT NULL,
	pick_up_location varchar(100) NOT NULL,
	drop_off_location varchar(100) NOT NULL,
	status varchar(50) DEFAULT 'requested'::character varying NULL,
	CONSTRAINT rides_pkey PRIMARY KEY (ride_id),
	CONSTRAINT rides_status_check CHECK (((status)::text = ANY ((ARRAY['requested'::character varying, 'assigned'::character varying, 'in progress'::character varying, 'completed'::character varying])::text[])))
);


-- public.rides foreign keys

ALTER TABLE public.rides ADD CONSTRAINT rides_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


CREATE TABLE public.payment (
	payment_id bigserial NOT NULL,
	customer_id int4 NULL,
	service_type varchar(50) NOT NULL,
	service_id int4 NOT NULL,
	amount numeric(10, 2) NOT NULL,
	CONSTRAINT payment_pkey PRIMARY KEY (payment_id),
	CONSTRAINT payment_service_type_check CHECK (((service_type)::text = ANY ((ARRAY['order'::character varying, 'ride'::character varying])::text[])))
);


-- public.payment foreign keys

ALTER TABLE public.payment ADD CONSTRAINT payment_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id);


CREATE TABLE public.driver_assignment (
	driver_id int4 NULL,
	service_type varchar(50) NOT NULL,
	service_id int4 NOT NULL,
	CONSTRAINT driver_assignment_service_type_check CHECK (((service_type)::text = ANY ((ARRAY['order'::character varying, 'ride'::character varying])::text[])))
);


-- public.driver_assignment foreign keys

ALTER TABLE public.driver_assignment ADD CONSTRAINT driver_assignment_driver_id_fkey FOREIGN KEY (driver_id) REFERENCES public.drivers(driver_id);