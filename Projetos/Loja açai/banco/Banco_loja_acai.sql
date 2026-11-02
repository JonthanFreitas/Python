-- Banco de dados da Loja de Açaí da Debys
create database if not exists loja_acai;

use loja_acai;

-- Clientes: telefone e e-mail não podem se repetir
create table cliente (
    id int auto_increment primary key,
    nome varchar(100) not null,
    telefone varchar(20) not null,
    email varchar(50) not null,
    senha varchar(100) not null,
    constraint uk_cliente_telefone unique (telefone),
    constraint uk_cliente_email unique (email)
);

-- Produtos: tamanho só P, M ou G e o mesmo produto não se repete no mesmo tamanho
create table produtos (
    id int auto_increment primary key,
    nome varchar(50) not null,
    tamanho char(1) not null,
    preco decimal(10,2) not null check (preco >= 0),
    constraint ck_produto_tamanho check (tamanho in ('P', 'M', 'G')),
    constraint uk_produto_nome_tamanho unique (nome, tamanho)
);

-- Pedidos: cada pedido pertence a um cliente
create table pedido (
    id int auto_increment primary key,
    clienteId int not null,
    data_pedido date not null,
    foreign key (clienteId) references cliente(id)
);

-- Itens do pedido: produtos de cada pedido (valor = preço unitário na hora da compra)
create table itens_pedido (
    id int auto_increment primary key,
    pedidoId int not null,
    produtoId int not null,
    quantidade int not null,
    valor decimal(10,2) not null,
    constraint ck_item_quantidade check (quantidade > 0),
    constraint ck_item_valor check (valor >= 0),
    foreign key (pedidoId) references pedido(id),
    foreign key (produtoId) references produtos(id)
);

-- Cardápio inicial
insert into produtos (nome, tamanho, preco) values
('Cupuaçu', 'P', 9.00),
('Cupuaçu', 'M', 14.00),
('Cupuaçu', 'G', 18.00),
('Açaí', 'P', 11.00),
('Açaí', 'M', 14.00),
('Açaí', 'G', 20.00);