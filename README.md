Archivo README - Proyecto Blockchain.
 A continuación, encontrarás información importante sobre el código y cómo utilizarlo.

Descripción
Este proyecto implementa un ejemplo básico de una cadena de bloques (blockchain) utilizando Python. La cadena de bloques contiene bloques que registran transacciones entre diferentes billeteras (wallets). Cada bloque contiene un conjunto de transacciones y está asegurado mediante cálculos hash y la estructura de un árbol de Merkle.

Uso
Ejecución del Código: Para ejecutar el código, simplemente coloca el fragmento en un archivo Python y asegúrate de tener la librería hashlib instalada (puedes instalarla con pip install hashlib).

Ejemplo de Uso: El código proporciona un ejemplo de uso simulando una cadena de bloques con transacciones y la creación de bloques. Puedes utilizarlo como guía para comprender cómo funciona la implementación.

Personalización: Si deseas adaptar este código para un caso específico o agregar más funcionalidades, asegúrate de entender cómo se estructura y cómo interactúan las clases.

Clases Principales
Blockchain: Representa la cadena de bloques en sí, donde se almacenan y gestionan los bloques.
Wallet: Modelo básico de una billetera que tiene un ID y un saldo.
Transaction: Simula una transacción entre dos billeteras.
MerkleTree: Implementa el cálculo del árbol de Merkle para las transacciones en un bloque.
Block: Representa un bloque en la cadena de bloques, contiene transacciones y mantiene integridad a través de cálculos hash.
Ejecución
Ejecuta el código y observa el ejemplo proporcionado. Asegúrate de entender cómo se crean transacciones, cómo se calcula el árbol de Merkle y cómo se agregan bloques a la cadena de bloques.

Si deseas personalizarlo, modifica las clases según tus necesidades y experimenta con diferentes escenarios de transacciones y bloques.

Contribuciones
Este proyecto es un ejemplo básico y puede expandirse de muchas maneras. Si deseas contribuir, considera agregar funcionalidades como persistencia en disco, verificación de integridad, validación de transacciones más complejas, entre otras.

¡Diviértete explorando y aprendiendo sobre cadenas de bloques con este proyecto! Si tienes alguna pregunta, no dudes en preguntar.
