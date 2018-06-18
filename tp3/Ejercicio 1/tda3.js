
var NUM_FILAS = 10;			//Numero de filas
var NUM_COLUMNAS = 100; 	//Numero de columnas

var NUM_BARCOS = 10;
var NUM_TURRETS = 1;

var GRID_DAMAGE_MAX = 10;
var GRID_DAMAGE_MIN = 1;

var LIFE_MIN = 20;
var LIFE_MAX = 200;

var grid;		//grilla 2d de daños
var ships;		//vector de barcos
var turrets;		//vector de turrets

var relativedamagegrid;		//grilla de daño relativo, considerando la vida de cada barco

var attackimage;		//lo usaremos para dinámico
var p=0;		//la cantidad de puntos que recibe el jugador B

Init();
function Init()
{
	Grid_Initialize();
	
	Ships_Initialize();
	Turrets_Initialize();

	RelativeDamageGrid_Initialize();		//lo usaremos para dinámico
	
	Grid_InitializeWithUniformDistribution();
	RelativeDamageGrid_Calculate();			//lo usaremos para dinámico
	
	console.log(grid);

	AttackImage_Initialize();				//lo usaremos para dinámico
	AttackImage_InitializeWithZeroes();	//lo usaremos para dinámico
}


function Grid_Initialize()
{
	grid = new Array(NUM_FILAS);
	for (var i=0; i < NUM_FILAS; i++)
	{
		grid[i] = new Array(NUM_COLUMNAS);
	}
	//x[5][12] = 3.0;	
}

function RelativeDamageGrid_Initialize()
{
	relativedamagegrid = new Array(NUM_FILAS);
	for (var i=0; i < NUM_FILAS; i++)
	{
		relativedamagegrid[i] = new Array(NUM_COLUMNAS);
	}
	//x[5][12] = 3.0;	
}


function AttackImage_Initialize()
{
	attackimage = new Array(NUM_FILAS);
	for (var i=0; i < NUM_FILAS; i++)
	{
		attackimage[i] = new Array(NUM_COLUMNAS);
	}
	//x[5][12] = 3.0;	
}

function AttackImage_InitializeWithZeroes()
{
	for (var i=0; i < NUM_FILAS; i++)
	{
		for (var j=0; j < NUM_COLUMNAS; j++)
		{
			attackimage[i][j] = 0;
		}
	}
}



function Grid_InitializeWithZerores()
{
	for (var i=0; i < NUM_FILAS; i++)
	{
		for (var j=0; j < NUM_COLUMNAS; j++)
		{
			grid[i][j] = 0;
		}
	}
}

function Grid_InitializeWithUniformDistribution()
{
	for (var i=0; i < NUM_FILAS; i++)
	{
		for (var j=0; j < NUM_COLUMNAS; j++)
		{
			grid[i][j] = RandomBetween(GRID_DAMAGE_MIN, GRID_DAMAGE_MAX);
		}
	}	
}

function RelativeDamageGrid_Calculate()
{
	for (var i=0; i < NUM_FILAS; i++)
	{
		for (var j=0; j < NUM_COLUMNAS; j++)
		{
			var life = ships[i].life;
			relativedamagegrid[i][j] = grid[i][j] / life;
		}
	}	
}


function RandomBetween(min, max)
{
	return Math.floor(Math.random() * max) + min;  	
}




function Ships_Initialize()
{
	ships = new Array(NUM_BARCOS);
	
	//cargamos los barcos:
	for (var i=0; i < NUM_BARCOS; i++)
	{
		ships[i] = {};
		ships[i].ID = i;
		ships[i].row = i;
		ships[i].column = 0;
		ships[i].isDead = false;
		ships[i].life = RandomBetween(LIFE_MIN, LIFE_MAX);
	}
}

function Ships_ThereExistsOneNotDead()
{
	for (var i=0; i < NUM_BARCOS; i++)
	{
		if (!ships[i].isDead) return true;
	}
	return false;
}


function Ships_AdvanceToTheRight()
{
	for (var i=0; i < NUM_BARCOS; i++)
	{
		if ( !ships[i].isDead )
		{
			ships[i].column++;
			p++;
		}
	}
	
}



function Turrets_Initialize()
{
	turrets = new Array(NUM_TURRETS);
	
	for (var i=0; i < NUM_TURRETS; i++)
	{
		turrets[i] = {};
		turrets[i].ID = i;
	}
}


function Turret_ShootToRow(row)
{
	//le disparo a una fila. Siempre habrá uno y solo un barco, en esa fila.
	var column = ships[row].column;
	ships[row].life = ships[row].life - grid[row][column];
	
	if (ships[row].life <= 0)
	{
		ships[row].isDead = true;
	}
}


function Turret_ShootToRowWithAllTurrets(row)
{
	for (var i=0; i < NUM_TURRETS; i++)
	{
		Turret_ShootToRow(row);
	}
}


function Player_RecalculateGreedy()
{
	//para cada barco, calculo en esta posición el número máximo de avances posibles disparándole con una torreta en esa fila.
	for (var i=0; i < NUM_BARCOS; i++)
	{
		if ( !ships[i].isDead )
		{
			var maxadvances = 0;
			var s = 0;
			var column = ships[i].column;
			var startcolumn = column;
			while (s < ships[i].life)
			{
				s = s + grid[i][column];
				column++;
				maxadvances++;
			}
			ships[i].maxadvances = maxadvances;
		}
	}
	
}


function Player_GetRowNumberToAttackGreedy()
{
	//esta función me devuelve el ID del barco (ie. el número de fila) que tengo que atacar, siguiendo la estrategia Greedy.
	
	Player_RecalculateGreedy();

	var min_maxadvances = 1000000;
	var min_i = -1;		//el ID del barco que atacaremos con la torreta.
	
	for (var i=0; i < NUM_BARCOS; i++)
	{
		if ( !ships[i].isDead )
		{			
			if ( ships[i].maxadvances < min_maxadvances )
			{
				min_maxadvances = ships[i].maxadvances;
				min_i = i;
			}
		}
	}
	
	if (min_i==-1)
	{
		alert("GUARDA!!");
	}
	
	return min_i;
}


function Player_PlayOneTurnGreedy()
{
	//siempre con una turret:
	
	//avanzo los barcos:
	Ships_AdvanceToTheRight();
	console.log("Avanzan los barcos hacia la derecha!");
	
	//obtengo la estrategia:
	var rowtoattack = Player_GetRowNumberToAttackGreedy();
	console.log("Greedy me sugiere que ataque la fila ", rowtoattack);
	
	Turret_ShootToRowWithAllTurrets(rowtoattack);
	console.log("Disparamos a la fila ", rowtoattack);

	console.log("Los barcos quedan asi:");
	console.log( JSON.stringify(ships) );
}



function Player_PlayGreedy()
{
	var numturnos = 0;
	while ( Ships_ThereExistsOneNotDead() )
	{
		numturnos++;
		Player_PlayOneTurnGreedy();
		console.log(ships);
		console.log("numturno: ", numturno);
		console.log("puntos: ", p);
	}
	console.log("El juego terminó. El jugador B obtuvo: ", p, " puntos");
	console.log("Numero de turnos:", numturnos);
	console.log("Total de puntos:", p);
}







////////////////////////////////////////////////////////////////////////////////////////

function Player_PlayDynamicExec()
{
	var numturnos = 0;
	while ( Ships_ThereExistsOneNotDead() )
	{
		numturnos++;
		Player_PlayDynamicDo();
		console.log(ships);
		console.log("numturno: ", numturno);
		console.log("puntos: ", p);
	}
	console.log("El juego terminó. El jugador B obtuvo: ", p, " puntos");
	console.log("Numero de turnos:", numturnos);
	console.log("Total de puntos:", p);
}


function Player_PlayDynamicDo()
{
	for (var j=0; j < NUM_COLUMNAS; j++)
	{
		Player_PlayDynamic(j);
	}
}


function Player_PlayDynamic(j)
{
	var turretsavailable = NUM_TURRETS;
	for (var i=0; i < NUM_BARCOS; i++)
	{
		for (var k=GRID_DAMAGE_MAX; k>=0; k--)
		{
			if ( grid[j][i]==k && !ships[i].isDead )
			{
				//atacar!
				ships[i].life = ships[i].life - grid[j][i];
				turretsavailable --;
				
				if (ships[i].life <= 0)
				{
					ships[i].isDead = true;
				}
				
			}
		}
	}
	
}




////////////////////////////////////////////////////////////////////////////////////////




function ParseDefinitions()
{
	var definitions = $('.definitions').val();
	alert(definitions);
	
	var defs = 	definitions.split(/\r?\n/);
	console.log(defs);
	
	for (var i=0; i < defs.length; i++)
	{
		var res = defs[i].split(" ");
		console.log(res);
		ships[i].life = res[0];
		
		for (var j=1; j < res.length; j++)
		{
			grid[i][j] = res[j];
		}
	}
	NUM_BARCOS = i;
}


////////////////////////////////////////////////////////////////////////////////////////

function InitGreedy()
{
	Grid_Initialize();
	Ships_Initialize();
	Turrets_Initialize();

	Grid_InitializeWithZerores();
	ParseDefinitions();
	
	console.log(grid);
	
	Player_PlayGreedy();
}


function InitDinamico()
{
	Grid_Initialize();
	Ships_Initialize();
	Turrets_Initialize();

	Grid_InitializeWithZerores();
	ParseDefinitions();
	
	console.log(grid);
	
	Player_PlayDynamicExec();
}
