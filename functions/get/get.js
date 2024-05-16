const catalyst = require('zcatalyst-sdk-node');
module.exports = (context, basicIO) => {

	const mazeId = basicIO.getArgument('maze-id');
	if (!mazeId) {
		basicIO.setStatus(400);
		basicIO.write('Invalid maze ID');
		context.close();
		return;
	}

	const app = catalyst.initialize(context);
	const datastore = app.datastore();
	const table = datastore.table('maze_data');
	table.getRow(parseInt(mazeId)).then((row) => {
		const data = row["maze-data"]
		basicIO.write(data);
		context.close();
	})
};
