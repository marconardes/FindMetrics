package testmm;



import java.awt.Color;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.apache.log4j.BasicConfigurator;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RefineryUtilities;
import org.repodriller.RepoDriller;

public class Graf extends ApplicationFrame {

    /**
     * Creates a new demo.
     *
     * @param title  the frame title.
     */
	
	static Map<String,List<Integer>> repoProcess;
	
    public Graf(final String title) {

        super(title);

        final XYDataset dataset = createDataset();
        final JFreeChart chart = createChart(dataset);
        final ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new java.awt.Dimension(500, 270));
        setContentPane(chartPanel);
        
    }
    
    /**
     * Creates a sample dataset.
     * 
     * @return a sample dataset.
     */
    private XYDataset createDataset() {
        
    	final List<XYSeries> series = new ArrayList<XYSeries>();

        for (String key : repoProcess.keySet()) {
            
        	int i = 0;
            List<Integer> value = repoProcess.get(key);
            final XYSeries series1 = new XYSeries(key);
            
            for(Integer points:value)
            {
            	i++;
            	series1.add(i,points);
            }
            series.add(series1);
     }
        
        

        final XYSeriesCollection dataset = new XYSeriesCollection();
       
        
        
        for (XYSeries xySeries : series) {
        
        	
        	if(xySeries.getKey().toString().contains("exp1groupB")||xySeries.getKey().toString().contains("Nardes"))
        	{
        		System.out.println(xySeries.getKey());
        	}
        	
        	dataset.addSeries(xySeries);
			
		}
        
        return dataset;
        
    }
    
    /**
     * Creates a chart.
     * 
     * @param dataset  the data for the chart.
     * 
     * @return a chart.
     */
    private JFreeChart createChart(final XYDataset dataset) {
        
        // create the chart...
        final JFreeChart chart = ChartFactory.createXYLineChart(
            "Linhas de codigo por commit",      // chart title
            "Commit",                      // x axis label
            "Linhas de codigo",                      // y axis label
            dataset,                  // data
            PlotOrientation.VERTICAL,
            true,                     // include legend
            true,                     // tooltips
            false                     // urls
        );

        chart.setBackgroundPaint(Color.white);

        final XYPlot plot = chart.getXYPlot();
        plot.setBackgroundPaint(Color.lightGray);
        plot.setDomainGridlinePaint(Color.white);
        plot.setRangeGridlinePaint(Color.white);
        
        final XYLineAndShapeRenderer render = new XYLineAndShapeRenderer();
        render.setSeriesShapesVisible(0, true);
        render.setSeriesPaint(0, Color.RED);
        render.setSeriesShapesVisible(1, true);

        render.setSeriesPaint(1, Color.BLUE);
        render.setSeriesShapesVisible(2, true);
        render.setSeriesPaint(2, Color.RED);
        render.setSeriesShapesVisible(3, true);
        render.setSeriesPaint(3, Color.BLUE);
        render.setSeriesShapesVisible(4, true);
        render.setSeriesPaint(4, Color.BLUE);
        render.setSeriesShapesVisible(5, false);
        render.setSeriesShapesVisible(6, false);
        render.setSeriesShapesVisible(7, false);
        render.setSeriesShapesVisible(8, false);
        
        
        
        plot.setRenderer(render);

        final NumberAxis rangeAxis = (NumberAxis) plot.getRangeAxis();
        rangeAxis.setStandardTickUnits(NumberAxis.createIntegerTickUnits());
                
        return chart;
        
    }


    /**
     * Starting point for the demonstration application.
     *
     * @param args  ignored.
     */
    public static void main(final String[] args) {

    	//RepodrillerMinner h= new RepodrillerMinner();
    	//BasicConfigurator.configure();
    	//new RepoDriller().start(h);
		
		CsvReader reader = new CsvReader();
		reader.read("devs.csv");
		System.out.println(reader.repoProcess.toString());
		repoProcess = reader.repoProcess;
    	
    	final Graf demo = new Graf("Linhas de codigo");
        
        
	
		
        
		
        demo.pack();
        RefineryUtilities.centerFrameOnScreen(demo);
        demo.setVisible(true);

    }

}