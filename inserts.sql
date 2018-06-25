INSERT INTO PESSOA VALUES ('330.555.777-99', 'Joao Pereira de Souza Siqueira', 'josiq321@gmail.com', 'Sao Paulo');
INSERT INTO PESSOA VALUES ('331.555.777-99', 'Bruno Wlakswatson', 'bruwlaks@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('332.555.777-99', 'Rafael Moura', 'rafamoura@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('333.555.777-99', 'Gabriel Cardoso', 'gabcard@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('334.555.777-99', 'Evert Abreu', 'evertbreu@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('335.555.777-99', 'Lucas Bezerra', 'lucasbezerra@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('336.555.777-99', 'Leonardo de Barros', 'leonardobarros@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('337.555.777-99', 'Eduardo Freitas', 'eduardofreitas@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('338.555.777-99', 'Gabriela Fernandes', 'gabnandes@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('339.555.777-99', 'Marilia Ferreira', 'eduardofreitas@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('310.555.777-99', 'Ana Paula Percival', 'anapercival@gmail.com', NULL);
INSERT INTO PESSOA VALUES ('311.555.777-99', 'Fernando Coelho', 'fernandcoelho@gmail.com', NULL);

INSERT INTO CLIENTE VALUES ('330.555.777-99');
INSERT INTO CLIENTE VALUES ('331.555.777-99');

INSERT INTO FUNCIONARIO VALUES ('330.555.777-99', 2000.00, 'Garcom');
INSERT INTO FUNCIONARIO VALUES ('331.555.777-99', 2100.00, 'Garcom');
INSERT INTO FUNCIONARIO VALUES ('311.555.777-99', 2200.00, 'Cozinheiro');
INSERT INTO FUNCIONARIO VALUES ('332.555.777-99', 2300.00, 'Cozinheiro');

INSERT INTO ESPECIALISTA VALUES ('333.555.777-99', 'Chef', 80.00);
INSERT INTO ESPECIALISTA VALUES ('334.555.777-99', 'Chef', 81.00);
INSERT INTO ESPECIALISTA VALUES ('335.555.777-99', 'Maitre', 82.00);
INSERT INTO ESPECIALISTA VALUES ('336.555.777-99', 'Maitre', 83.00);
INSERT INTO ESPECIALISTA VALUES ('337.555.777-99', 'Copeiro', 84.00);
INSERT INTO ESPECIALISTA VALUES ('338.555.777-99', 'Copeiro', 85.00);
INSERT INTO ESPECIALISTA VALUES ('339.555.777-99', 'Bartender', 86.00);
INSERT INTO ESPECIALISTA VALUES ('310.555.777-99', 'Bartender', 87.00);

INSERT INTO BARTENDER VALUES ('339.555.777-99');
INSERT INTO BARTENDER VALUES ('310.555.777-99');

INSERT INTO COPEIRO VALUES ('337.555.777-99');
INSERT INTO COPEIRO VALUES ('338.555.777-99');

INSERT INTO CHEF VALUES ('333.555.777-99');
INSERT INTO CHEF VALUES ('334.555.777-99');

INSERT INTO MAITRE VALUES ('335.555.777-99');
INSERT INTO MAITRE VALUES ('336.555.777-99');

INSERT INTO TELEFONES VALUES('330.555.777-99', '(16) 9034-5217');
INSERT INTO TELEFONES VALUES('330.555.777-99', '(19) 9385-2849');
INSERT INTO TELEFONES VALUES('331.555.777-99', '(19) 8309-3213');
INSERT INTO TELEFONES VALUES('332.555.777-99', '(11) 9788-3345');
INSERT INTO TELEFONES VALUES('333.555.777-99', '(11) 9660-1123');
INSERT INTO TELEFONES VALUES('334.555.777-99', '(11) 9923-4532');

-- Duração se refere a quantidade de meses
INSERT INTO CONTRATO_ESPECIALISTA VALUES ('333.555.777-99', to_date('17/06/2017', 'DD/MM/YYYY'), 12, 0); 
INSERT INTO CONTRATO_ESPECIALISTA VALUES ('334.555.777-99', to_date('12/12/2017', 'DD/MM/YYYY'), 6, 0); 

-- Permite funcionaro e cliente serem a mesma pessoa
INSERT INTO EVENTO VALUES ('330.555.777-99', to_date('22/09/2016', 'DD/MM/YY'), 'Casamento', 3000.00, 'A vista', 1000);
INSERT INTO EVENTO VALUES ('330.555.777-99', to_date('01/01/2017', 'DD/MM/YY'), 'Casamento', NULL, NULL, NULL);
INSERT INTO EVENTO VALUES ('331.555.777-99', to_date('05/01/2017', 'DD/MM/YY'), 'Formatura', 4000.00, 'Parcelado em 6x', 2000);
INSERT INTO EVENTO VALUES ('331.555.777-99', to_date('10/10/2016', 'DD/MM/YY'), 'Formatura', NULL, NULL, NULL);

INSERT INTO FUNCIONARIO_EVENTO VALUES ('311.555.777-99', '330.555.777-99', to_date('22/09/2016', 'DD/MM/YY'));
INSERT INTO FUNCIONARIO_EVENTO VALUES ('332.555.777-99', '330.555.777-99', to_date('01/01/2017', 'DD/MM/YY'));

INSERT INTO LOCAL VALUES (DEFAULT, '33884-933', 3224, NULL, 'Rua Alexandrina', 'Sao Carlos', 1000, 'Salao');
INSERT INTO LOCAL VALUES (DEFAULT, '33756-180', 1222, NULL, 'Rua Alfredo Campos', 'Piracicaba', 2000, 'Salao');
INSERT INTO LOCAL VALUES (DEFAULT, '85656-890', 4324, NULL, 'Rua Erasmo Carlos', 'Rio de Janeiro', 1500, 'Campo');
INSERT INTO LOCAL VALUES (DEFAULT, '30956-120', 9066, NULL, 'Rua 9 de Julho', 'Sao Jose dos Campos', 1700, 'Campo');

INSERT INTO SALAO VALUES (1);
INSERT INTO SALAO VALUES (2);

INSERT INTO CAMPO VALUES (3);
INSERT INTO CAMPO VALUES (4);

-- Formatura pode se referenciar a um evento que na verdade é casamento (tratar em aplicação)
INSERT INTO FORMATURA VALUES ('331.555.777-99', to_date('05/01/2017', 'DD/MM/YY'), '339.555.777-99', '337.555.777-99', 1); 
INSERT INTO FORMATURA VALUES ('331.555.777-99', to_date('10/10/2016', 'DD/MM/YY'), NULL, NULL, 2);

-- Casamento pode se referenciar a um evento que na verdade é formatura (tratar em aplicação)
INSERT INTO CASAMENTO VALUES ('330.555.777-99', to_date('22/09/2016', 'DD/MM/YY'), '333.555.777-99','335.555.777-99', 3); 
INSERT INTO CASAMENTO VALUES ('330.555.777-99', to_date('01/01/2017', 'DD/MM/YY'), NULL, NULL, 4);

INSERT INTO CARDAPIO VALUES ('330.555.777-99', to_date('22/09/2016', 'DD/MM/YY'), 25);
INSERT INTO CARDAPIO VALUES ('330.555.777-99', to_date('01/01/2017', 'DD/MM/YY'), 30);
INSERT INTO CARDAPIO VALUES ('331.555.777-99', to_date('05/01/2017', 'DD/MM/YY'), 35);
INSERT INTO CARDAPIO VALUES ('331.555.777-99', to_date('10/10/2016', 'DD/MM/YY'), 40);

INSERT INTO ITEM VALUES ('Mignon ao molho madeira');
INSERT INTO ITEM VALUES ('Pernil desossado');

INSERT INTO CARDAPIO_ITEM VALUES ('330.555.777-99', to_date('22/09/2016', 'DD/MM/YY'), 'Mignon ao molho madeira');
INSERT INTO CARDAPIO_ITEM VALUES ('330.555.777-99', to_date('22/09/2016', 'DD/MM/YY'), 'Pernil desossado');
INSERT INTO CARDAPIO_ITEM VALUES ('330.555.777-99', to_date('01/01/2017', 'DD/MM/YY'), 'Mignon ao molho madeira');
INSERT INTO CARDAPIO_ITEM VALUES ('331.555.777-99', to_date('05/01/2017', 'DD/MM/YY'), 'Pernil desossado');
INSERT INTO CARDAPIO_ITEM VALUES ('331.555.777-99', to_date('10/10/2016', 'DD/MM/YY'), 'Pernil desossado');

INSERT INTO INGREDIENTES VALUES ('Mignon ao molho madeira', 'Manteiga');
INSERT INTO INGREDIENTES VALUES ('Mignon ao molho madeira', 'Amido de milho');
INSERT INTO INGREDIENTES VALUES ('Mignon ao molho madeira', 'Champignon');
INSERT INTO INGREDIENTES VALUES ('Mignon ao molho madeira', 'Cebola');
INSERT INTO INGREDIENTES VALUES ('Mignon ao molho madeira', 'Alho');
INSERT INTO INGREDIENTES VALUES ('Mignon ao molho madeira', 'Vinho tinto');
INSERT INTO INGREDIENTES VALUES ('Mignon ao molho madeira', 'Água');
INSERT INTO INGREDIENTES VALUES ('Pernil desossado', 'Pernil de porco desossado');
INSERT INTO INGREDIENTES VALUES ('Pernil desossado', 'Alho');
INSERT INTO INGREDIENTES VALUES ('Pernil desossado', 'Cebola');
INSERT INTO INGREDIENTES VALUES ('Pernil desossado', 'Vinho branco');
INSERT INTO INGREDIENTES VALUES ('Pernil desossado', 'Limão');
INSERT INTO INGREDIENTES VALUES ('Pernil desossado', 'Azeite');

INSERT INTO FORNECEDOR VALUES ('02.266.600/0001-21', 'Walter Luis');
INSERT INTO FORNECEDOR VALUES ('78.735.523/0001-73', 'Aldemir Ferreira');

INSERT INTO PRODUTO VALUES ('Manteiga 1kg');
INSERT INTO PRODUTO VALUES ('Amido de milho 1kg');
INSERT INTO PRODUTO VALUES ('Champignon 500g');
INSERT INTO PRODUTO VALUES ('Cebola');
INSERT INTO PRODUTO VALUES ('Alho');
INSERT INTO PRODUTO VALUES ('Vinho tinto 1L');
INSERT INTO PRODUTO VALUES ('Água 5L');
INSERT INTO PRODUTO VALUES ('Pernil de porco desossado 1kg');
INSERT INTO PRODUTO VALUES ('Vinho branco 1L');
INSERT INTO PRODUTO VALUES ('Limão');
INSERT INTO PRODUTO VALUES ('Azeite 1L');

INSERT INTO FORNECIMENTO VALUES ('02.266.600/0001-21', 'Manteiga 1kg', to_date('17/12/2017', 'DD/MM/YYYY'), 10, 300.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('02.266.600/0001-21', 'Amido de milho 1kg', to_date('10/02/2018', 'DD/MM/YYYY'), 10, 150.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('02.266.600/0001-21', 'Champignon 500g', to_date('21/02/2018', 'DD/MM/YYYY'), 6, 180.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('02.266.600/0001-21', 'Cebola', to_date('30/02/2018', 'DD/MM/YYYY'), 30, 15.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('02.266.600/0001-21', 'Alho', to_date('05/03/2018', 'DD/MM/YYYY'), 20, 10.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('78.735.523/0001-73', 'Vinho tinto 1L', to_date('15/03/2018', 'DD/MM/YYYY'), 3, 210.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('78.735.523/0001-73', 'Água 5L', to_date('27/03/2018', 'DD/MM/YYYY'), 6, 30.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('78.735.523/0001-73', 'Pernil de porco desossado 1kg', to_date('06/04/2018', 'DD/MM/YYYY'), 5, 150.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('78.735.523/0001-73', 'Vinho branco 1L', to_date('12/04/2018', 'DD/MM/YYYY'), 8, 240.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('78.735.523/0001-73', 'Limão', to_date('01/05/2018', 'DD/MM/YYYY'), 25, 15.00, NULL);
INSERT INTO FORNECIMENTO VALUES ('78.735.523/0001-73', 'Azeite 1L', to_date('02/06/2018', 'DD/MM/YYYY'), 10, 200.00, NULL);

INSERT INTO ITEM_FORNECIMENTO VALUES ('02.266.600/0001-21', 'Manteiga 1kg', to_date('17/12/2017', 'DD/MM/YYYY'), 'Mignon ao molho madeira');
INSERT INTO ITEM_FORNECIMENTO VALUES ('02.266.600/0001-21', 'Amido de milho 1kg', to_date('10/02/2018', 'DD/MM/YYYY'), 'Mignon ao molho madeira');
INSERT INTO ITEM_FORNECIMENTO VALUES ('02.266.600/0001-21', 'Champignon 500g', to_date('21/02/2018', 'DD/MM/YYYY'), 'Mignon ao molho madeira');
INSERT INTO ITEM_FORNECIMENTO VALUES ('02.266.600/0001-21', 'Cebola', to_date('30/02/2018', 'DD/MM/YYYY'), 'Mignon ao molho madeira');
INSERT INTO ITEM_FORNECIMENTO VALUES ('02.266.600/0001-21', 'Alho', to_date('05/03/2018', 'DD/MM/YYYY'), 'Mignon ao molho madeira');
INSERT INTO ITEM_FORNECIMENTO VALUES ('78.735.523/0001-73', 'Vinho tinto 1L', to_date('15/03/2018', 'DD/MM/YYYY'), 'Mignon ao molho madeira');
INSERT INTO ITEM_FORNECIMENTO VALUES ('78.735.523/0001-73', 'Água 5L', to_date('27/03/2018', 'DD/MM/YYYY'), 'Mignon ao molho madeira');
INSERT INTO ITEM_FORNECIMENTO VALUES ('78.735.523/0001-73', 'Pernil de porco desossado 1kg', to_date('06/04/2018', 'DD/MM/YYYY'), 'Pernil desossado');
INSERT INTO ITEM_FORNECIMENTO VALUES ('78.735.523/0001-73', 'Vinho branco 1L', to_date('12/04/2018', 'DD/MM/YYYY'), 'Pernil desossado');
INSERT INTO ITEM_FORNECIMENTO VALUES ('78.735.523/0001-73', 'Limão', to_date('01/05/2018', 'DD/MM/YYYY'), 'Pernil desossado');
INSERT INTO ITEM_FORNECIMENTO VALUES ('78.735.523/0001-73', 'Azeite 1L', to_date('02/06/2018', 'DD/MM/YYYY'), 'Pernil desossado');

--COMMIT;
